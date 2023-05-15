"""
    TCP 服务端开发流程:
        1.创建服务端socket实例对象
        2.绑定端口号和IP地址-bind()
        3.listen()：监听
        4.等待接收客户端的连接请求：accept()
        5.处理请求:接收数据recv(),发送数据send()
        6.关闭程序:close()
"""
# 导入socket模块
import socket

if __name__ == '__main__':
    # 创建socket对象, 指定协议为ipv4, tcp传输
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置服务端端口复用
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定服务端ip
    socket_server.bind(('', 8080))
    # 设置客户端监听数量
    socket_server.listen(5)
    # 等待接收客户端请求, 定义变量接收处理客户端套接字对象和客户端IP信息
    print('等待客户端连接...')
    client_socket, client_address = socket_server.accept()
    # 打印接受到的请求地址信息
    print('客户端连接成功, 客户端ip为:{}, 端口为:{}'.format(client_address[0], client_address[1]))
    # 接收客户端数据并解码
    client_data = client_socket.recv(1024).decode()
    print('接收客户端数据: {}'.format(client_data))
    # 向客户端发送数据
    client_socket.send('服务端回复: 数据传输成功'.encode())
    # 关闭客户端处理套接字对象
    client_socket.close()
    # 关闭服务端套接字对象
    socket_server.close()
