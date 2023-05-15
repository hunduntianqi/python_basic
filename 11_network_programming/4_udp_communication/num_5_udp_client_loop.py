"""
    UDP 传输客户端开发 ==> 循环交流
"""
import socket

if __name__ == '__main__':
    # 创建socket对象, 指定传输协议为UDP传输
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 连接服务端
    # socket_client.connect(('', 8080)) UDP 传输对象不支持
    while True:
        # 向服务端发送数据
        client_data = input('My to Server:\n')
        socket_client.sendto(client_data.encode(), ('127.0.0.1', 8080))
        if client_data == 'exit':
            print('客户端关闭, 溜了溜了....')
            break
        # 接收服务端数据
        server_data, address_server = socket_client.recvfrom(1024)
        print('服务端:{}'.format(server_data.decode()))
    # 客户端关闭
    socket_client.close()
