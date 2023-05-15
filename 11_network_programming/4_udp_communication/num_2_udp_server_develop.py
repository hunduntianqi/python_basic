"""
    UDP 传输服务端开发
"""
# 导入socket模块
import socket

if __name__ == '__main__':
    # 创建socket对象, 指定传输协议为UDP传输
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置端口复用
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定ip和端口
    socket_server.bind(('', 8080))
    # 设置监听
    # socket_server.listen(5) UDP传输对象不支持监听操作
    # 等待接收客户端连接
    print('等待接收客户端数据...')
    # client_socket, address = socket_server.accept() UDP对象不支持
    client_data, address = socket_server.recvfrom(1024)  # 接收UDP数据 ==> recvfrom()
    print('收到客户端[{}:{}]数据...'.format(address[0], address[1]))
    print('client_data:{}'.format(client_data.decode()))
    # 向客户端发送数据
    socket_server.sendto('已收到你的数据, 一切正常！！'.encode(), address)
    # 关闭与客户端连接
    socket_server.close()
