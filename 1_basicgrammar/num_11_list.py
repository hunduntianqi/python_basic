"""
    列表 ==> list:
        1）python中使用最频繁的数据类型,在其他语言通常叫做数组
        2）专门用于存储一串信息
        3）列表用[]定义, 数据之间用英文逗号 , 分隔
        4）列表的索引从 0 开始
        列表定义格式:
            格式一: list_name = []
            格式二: list_name = list(可迭代对象)
        列表常用方法:
            1.列表.insert(索引,数据): 在指定位置插入数据
            2.列表.append(数据): 在列表末尾追加数据
            3.列表.extend(列表2): 将列表2的数据追加到列表
            4.del 列表[索引]: 删除指定索引的数据
            5.列表[索引] = 数据: 修改指定索引的数据
            6.列表.remove[数据]: 删除第一个出现的指定数据
            7.列表.pop: 删除列表末尾的数据, 并返回被删除的数据
            8.列表.pop[索引]: 删除指定索引的数据, 并返回被删除的数据
            9.列表.clear: 清空列表
            10.len(列表): 统计列表长度
            11.列表.count(数据): 统计数据在列表中出现的次数
            12.列表.sort(): 默认升序排序; 列表.sort(rever=True): 降序排序
            13.列表.reverse: 列表翻转,逆序
            14.列表.index(数据): 取列表中对应数据的索引值
        列表转换为元组 ==> tuple(list_name)
        列表推导式:
            根据可迭代对象, 简单的构建列表
            语法: list_name = [表达式 for 变量名 in 可迭代对象 if 筛选条件(可省略)]
"""

if __name__ == '__main__':
    # 使用range()函数创建数字列表
    list_num1 = list(range(1, 10))
    print(list_num1)

    # 指定range()函数步长, 创建包含1-10以内偶数列表
    list_num2 = list(range(2, 11, 2))
    print(list_num2)

    # 使用列表推导式创建列表
    list_num3 = [value ** 3 for value in range(10)]
    print(list_num3)
    # 使用列表推导式创建10-30之间能被3或5整除的数字
    list_num4 = [value for value in range(10, 30) if value % 3 == 0 or value % 5 == 0]
    print(list_num4)
