"""
    UDP 传输客户端开发
"""
import socket

if __name__ == '__main__':
    # 创建socket对象, 指定传输协议为UDP传输
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 连接服务端
    # socket_client.connect(('', 8080)) UDP 传输对象不支持
    # 向服务端发送数据
    socket_client.sendto('你好, 我是一号客户端, 现在测试程序是否正常, 收到请回复'.encode(),
                         ('127.0.0.1', 8080))
    # 接收服务端数据
    server_data, address_server = socket_client.recvfrom(1024)
    print('服务端:{}'.format(server_data.decode()))
