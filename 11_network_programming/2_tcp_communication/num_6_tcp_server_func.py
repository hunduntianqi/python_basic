"""
    TCP 服务端函数版本:
        1. 定义主函数, 完成创建socket, 绑定地址, 监听客户端连接, 接收客户端请求等操作
        2. 定义客户端请求处理函数, 完成与客户端的通信
"""
# 导入socket模块
import socket


# 定义客户端请求处理函数
def client_request_handle(client_request_socket: socket.socket):
    # while循环保证不断处理客户端请求
    while True:
        # 接收客户端数据
        client_data = client_request_socket.recv(1024)
        # 判断客户端是否关闭
        if not client_data:
            print('客户端关闭, 无需再处理请求, 关闭服务器...')
            break
        print('客户端:{}'.format(client_data.decode()))
        # 回复客户端, 向客户端发送数据
        server_input = input('My to Client:')
        client_request_socket.send(server_input.encode())
    # 关闭套接字对象
    client_request_socket.close()


# 定义主函数
def main():
    # 创建socket对象
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # print(type(socket_server))
    # 绑定ip和端口
    socket_server.bind(('', 8080))
    # 设置客户端监听数量
    socket_server.listen(5)
    # 等待接收客户端请求, 获取客户端请求处理socket对象
    print("等待客户连接...")
    client_request_socket, client_address = socket_server.accept()
    # 打印客户端地址
    print('客户端ip:{}:{}'.format(client_address[0], client_address[1]))
    # 调用函数, 处理客户端请求
    client_request_handle(client_request_socket)
    # 关闭服务器对象
    socket_server.close()


if __name__ == '__main__':
    main()
