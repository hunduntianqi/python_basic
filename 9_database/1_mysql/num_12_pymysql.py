"""
    pymysql ==> python中用来操作mysql数据库的第三方包
        1.导入pymysql包 == > import pymysql
        2.创建连接对象
            调用pymysql模块中的connect()函数来创建连接对象,代码如下:
                mysql_conn = pymysql.connect(host, port, user, password, database, charset)
                host ==> 连接的MySQL主机地址, 如果是本机是 'localhost' / '127.0.0.1'
                port ==> 连接的MySQL主机端口, 默认是3306
                user ==> 用户名
                password ==> 登录密码
                database ==> 要操作的数据库名称
                charset ==> 通信采用的文本编码方式, 推荐使用utf-8
            连接对象操作说明:
                关闭连接 ==> mysql_conn.close()
                提交数据 ==> mysql_conn.commit()
                    注意: 如果 SQL 语句执行后目标是期望修改数据库数据, 则必须进行提交数据操作, 否则不会修改数据库数据
                撤销数据 ==> mysql_conn.rollback()
        3.获取游标对象:
            获取游标对象的目标是要执行sql语句,完成对数据库的增、删、改、查操作
            游标可以记录获取数据的个数, 第一次取出第一条数据, 第二次会从第二条数据开始读取, 类似迭代器
            调用连接对象的 cursor() 方法获取游标对象: cursor = mysql_conn.cursor()
            操作说明:
                3.1 使用游标执行SQL语句:execute(operation[parameters])执行SQL语句, 返回受影响的行数,
                    主要用于执行insert, update, delete, select等语句
                3.2 获取查询结果集中的一条数据: cursor.fetchone()返回一个元组, 如（1, '张三'）
                3.3 获取查询结果集中的所有数据: cursor.fetchall()返回一个嵌套元组, 如((1,'张三'),(2,'李四'))
                3.4 关闭游标:cursor.close(), 表示和数据库的操作完成, 断开数据库连接
        4. 定义Sql语句:
            增:
                sql = "insert into table_name(field_name1, field_name2, ...) values(value1, value2, ...);"
                sql = "insert into table_name values(value1, value2, ...);"
            删:
                sql = "delete from table_name where condition;"
                消除重复行 ==> sql = "select distinct field_name from table_name;"
                删除所有数据 ==> sql = "delete from table_name;"
            改:
                指定条件修改数据 ==> sql = "update table_name set field_name1=value1, field_name2=value2, ... where condition;"
                不指定条件修改数据 ==> sql = "update table_name set field_name1=value1, field_name2=value2, ...;"
            查:
                sql = "select * from table_name;"
    SQL注入:
        指通过SQL语句的漏洞, 盗取数据库的数据
        SQL注入无法彻底防止, 可以通过将关键参数使用占位符, 然后传参的形式来提高安全性, 减少Sql注入风险, 例:
            sql = "delete from user where user_id = %s;" ==> 定义Sql语句, 关键参数使用 %s 占位符占位
            cursor.execute(sql, [2]) ==> 执行Sql语句通过列表传参

"""
import pymysql


# 定义函数, 执行数据库添加数据操作
def insert_data(conn: pymysql.connections.Connection):
    # 定义Sql语句, 向数据库插入数据
    sql = 'insert into user(user_id, user_name, user_age, user_email) values(%s, %s, %s, %s)'
    # 获取游标对象
    cursor = conn.cursor()
    # 执行Sql数据
    cursor.execute(sql, [2, "郭鹏强", 22, "1729992141@qq.com"])
    cursor.execute(sql, [3, "陈欣妮", 25, "1729992141@qq.com"])
    # 提交数据, 修改数据库数据
    conn.commit()
    # 关闭游标对象
    cursor.close()


# 定义函数, 执行数据库删除数据操作
def delete_data(conn: pymysql.connections.Connection):
    # 获取游标对象
    cursor = conn.cursor()
    # 定义删除数据的Sql语句
    sql = "delete from user where user_id = %s;"
    # 执行Sql语句
    cursor.execute(sql, [2])
    # 提交数据
    conn.commit()
    # 关闭游标对象
    cursor.close()


# 定义函数, 执行修改数据操作
def update_data(conn: pymysql.connections.Connection):
    # 获取游标对象
    cursor = conn.cursor()
    # 定义修改数据的Sql语句
    sql = "update user set user_id=2 where user_id=3;"
    # 执行Sql语句
    cursor.execute(sql)
    # 提交数据
    conn.commit()
    # 关闭游标对象
    cursor.close()


# 定义函数, 执行查找数据库数据操作
def select_data(conn: pymysql.connections.Connection):
    # 获取游标对象
    cursor = conn.cursor()
    # 定义修改数据的Sql语句
    sql = "select * from stu where age < %s;"
    # 执行Sql语句
    cursor.execute(sql, [30])
    # 获取所有查询到的数据
    data_tuple = cursor.fetchall()
    for data in data_tuple:
        print(data)
    # 关闭游标对象
    cursor.close()


if __name__ == '__main__':
    # 获取数据库连接对象
    mysql_conn = pymysql.connect(host="localhost", port=3306, user='root', password='2251789949gpt',
                                 database='pythonstudy')
    # 调用函数, 执行Sql语句
    # insert_data(mysql_conn)
    # delete_data(mysql_conn)
    # update_data(mysql_conn)
    select_data(mysql_conn)
    # 释放资源
    mysql_conn.close()
