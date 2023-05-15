"""
    文件的读写操作:
        open(path, mode, encoding)函数:
            是python中创建文件对象的函数, 返回一个文件对象
            path: 文件路径, 可以是绝对路径, 也可以是相对路径
            mode: 操作模式, 分为 r -> 读, w -> 写, a -> 追加写入;
                  rb -> 二进制读, wb -> 二进制写, ab -> 二进制追加写入
            encoding: 文件编码, 操作二进制文件时, 不需要填写
        文件读取:
            a. 创建文件对象
                file = open(path, 'r', encoding = 'character_name')
            b. file.read(num):
                指定长度读取文件数据 ==> num ==> 读取文件字符数, 如果不指定num, 默认读取文件所有数据
            c. file.readlines():
                按行读取文件所有内容, 并存入列表, 每一行数据是列表一个元素
            d. file.readline():
                一次读取一行内容
            e. 关闭文件对象:
                file.close()
        文件写入:
            a. 创建文件对象
                file = open(path, 'w', encoding = 'character_name')
                注意:
                    如果文件存在, ‘w’ 模式会将文件内容清空, 再写入新的数据
                    如果文件不存在, ‘w’ 模式会创建文件, 再写入数据
            b. file.write(data)
                将数据写入内存, 此时数据存入缓冲区, 未真正存入文件
            c. file.flush():
                刷新文件内容, 将缓冲区数据写入文件, 避免一次写入过多数据造成阻塞
            d. file.close():
                关闭文件, 内置有flush()功能, 文件关闭前会将所有数据写入文件
        文件追加写入:
            a. 创建文件对象:
                file = open(path, 'a', encoding = 'character_name')
                注意:
                    如果文件存在, ‘a’ 模式会在文件原有的内容后写入新的数据
                    如果文件不存在, ‘a’ 模式会创建文件, 再写入数据
            b. file.write(data)
                将数据写入内存, 此时数据存入缓冲区, 未真正存入文件
            c. file.flush():
                刷新文件内容, 将缓冲区数据写入文件, 避免一次写入过多数据造成阻塞
            d. file.close():
                关闭文件, 内置有flush()功能, 文件关闭前会将所有数据写入文件
        with ... as ...: 上下文管理器
            格式: with open(path, mode, encoding) as file:
                     # 对文件的各种操作
            该方法可以自动关闭文件, 解除资源占用
"""
import time

if __name__ == '__main__':
    # 创建一个文件对象
    file = open('$1_file_encode.py', 'r', encoding='utf-8')
    data_num = file.readline()  # 读取一行数据
    print(data_num)
    list_file: list = file.readlines()  # 读取所有数据并按行存入列表
    print(list_file)
    for data in list_file:
        print(data)
    # 关闭文件对象
    file.close()
    time.sleep(3)

    # 文件写入操作
    file_write = open('test.txt', 'w', encoding='utf-8')
    # 数据写入内存
    file_write.write("混沌初开道为先")
    # 将数据从内存写入文件
    file_write.flush()
    print("数据写入成功")
    file_write.close()
