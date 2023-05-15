"""
    TCP 客户端开发流程:
         1.创建socket()对象
         2.和服务端socket创建连接connect()
         3/4:发送-send()/接收recv()数据
         5.关闭客户端socket-close()
     通过while循环改写客户端代码, 实现与服务端不断交流
"""
# 导入socket模块
import socket

if __name__ == '__main__':
    # 创建客户端socket对象, 指定协议为ipv4, tcp传输
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 指定服务端ip和端口, 与服务端创建连接
    socket_client.connect(('127.0.0.1', 8080))
    while True:
        client_input = input('My to Server:')
        if client_input == 'exit': # 客户端关闭, 循环退出条件
            print('客户端关闭...')
            break
        # 向服务端发送数据
        socket_client.send(client_input.encode())
        # 接收服务端数据
        server_data = socket_client.recv(1024)
        if not server_data:
            print('服务端出现异常, 关闭连接...')
            break
        print('服务端:{}'.format(server_data.decode()))
    # 关闭客户端socket对象
    socket_client.close()