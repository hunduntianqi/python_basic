"""
    使用socket构建静态服务器, 向浏览器发送提示数据
"""


import socket

# 创建socket对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 端口复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定地址信息
tcp_server_socket.bind(('', 8080))
# 设置监听
tcp_server_socket.listen(3)
# 设置循环使服务器不间断运行
while True:
    # 接受连接请求
    clien_socket, adds = tcp_server_socket.accept()
    # 接收数据并解码！！
    recv_data = clien_socket.recv(1024)
    if len(recv_data) == 0:
        print('客户端关闭！！！')
        break
    print(recv_data.decode())
    # 组装http响应报文：
    # 响应行：
    response_line = 'HTTP/1.1 200 OK\r\n'
    # 响应头：
    response_header = 'server:1.0\r\n'
    # 响应体
    response_body = '你好,Web的世界欢迎你！！！'
    # 发送数据
    clien_socket.send('{}{}\n{}'.format(response_line, response_header, response_body).encode('gbk'))
    # 关闭clien.socket
    clien_socket.close()
