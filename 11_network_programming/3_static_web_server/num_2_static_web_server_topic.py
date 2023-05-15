"""
    使用socket模块构建静态服务器, 向浏览器发送图片信息
"""
import os
import random
# 导入socket模块
import socket
import time
# 导入Thread类
from threading import Thread


# 定义函数用来读取特定文件的数据
def file_data() -> list:
    # 定义文件路径, 用于自定义文件路径
    path_dir: str = input('请输入图片文件夹路径:\n')
    # 定义变量接收文件数据
    file_data_list: list[bytes] = []
    # 获取存储所有图片名的列表
    list_pic = os.listdir(path_dir)
    # 遍历列表
    for pic_name in list_pic:
        try:
            # 组装图片路径
            path_pic = path_dir + '\\' + pic_name
            # 读取文件数据存入列表
            with open(path_pic, 'rb') as file:
                file_data_list.append(file.read())
        except:
            pass
    return file_data_list


# 定义函数处理客户单端请求
def client_request_handle(client_socket: socket.socket, address: tuple[str, int], list_pic: list):
    print('客户端[{}:{}]连接成功...'.format(address[0], address[1]))
    while True:
        # 接收客户端数据并解码
        client_data = client_socket.recv(1024).decode()
        # 判断客户端是否关闭
        if not client_data:
            print('客户端[{}:{}]已关闭...'.format(address[0], address[1]))
            break
        print(client_data)
        # 组装响应报文, 给浏览器返回数据
        # 响应行
        response_line = 'HTTP/1.1 200 OK\r\n'
        # 响应头:
        response_header = 'server:1.0\r\n'
        # 调用函数获取文件数据作为响应体
        response_body = random.choice(list_pic)
        # 组装响应数据, \n表示一个空行, 代表响应头结束
        response_data = '{}{}\n'.format(response_line, response_header).encode('gbk') + response_body
        # 将响应数据发送给浏览器
        client_socket.send(response_data)
        time.sleep(2)
    client_socket.close()


# 定义主函数
def main():
    # 创建socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定ip和端口
    server_socket.bind(('', 8080))
    # 设置监听
    server_socket.listen(5)
    print('等待客户端连接...')
    # 获取图片信息列表
    list_pic = file_data()
    while True:
        client_socket, address = server_socket.accept()
        sub_thread = Thread(target=client_request_handle, args=(client_socket, address, list_pic))
        sub_thread.start()
    # 关闭服务器
    server_socket.close()


if __name__ == '__main__':
    main()
