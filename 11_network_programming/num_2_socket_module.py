"""
    Socket:
        又称"套接字", 应用程序通常通过"套接字"向网络发出请求或者应答网络请求,
        使主机间或者一台计算机上的进程间可以通讯, 进程之间通信的一个工具
        作用: 负责进程之间的网络数据传输
    socket模块 ==> python中的网络通信相关模块
        创建socket对象:
            socket_object = socket.socket([family[, type[, protocol]]])
            family: 可以是 socket.AF_UNIX(ipv6) 或者 socket.AF_INET(ipv4)
            type:
                socket.SOCK_STREAM ==> TCP
                socket.SOCK_DGRAM ==> UDP
            protocol: 一般不填默认为 0
        socket对象内建函数:
            服务端:
                1. bind(): 用于绑定服务端地址和端口, 在AF_INET下, 以元组 ==> (host, port)表示
                           host ==> ip地址, 字符串形式, 不写默认为本机ip
                           port ==> 端口号, 数字形式
                2. listen(): 设置监听, 参数可以设置最大监听个数, 数字形式
                3. accept(): 被动接受TCP客户端的连接, 阻塞等待连接的到来, 返回值为一个元组
                             (处理客户端请求的socket对象, 客户端的地址信息(ip, port)), 元组拆包
                             获取socket对象与客户端地址信息:
                             client_socket, client_address = socket_object.accept()
            客户端:
                1. connect(): 连接服务器, 以元组形式指定服务端ip和端口 ==> ('ip', port), 如果连接出错,
                              返回 socket.error 错误
                2. connect_ex(): connect()函数的扩展版本, 出错时返回出错码, 而不是抛出异常
            公用函数:
                recv(bufsize): 接收数据, bufsize指定要接受的最大数据量
                send(str): 发送数据, 将str中的信息发送出去, 返回发送的字节数, 该数字可能小于str的字节数
                sendall(str): 发送数据, 将str中的数据全部发送出去, 成功返回None, 失败则抛出异常
                recvfrom(bufsize): 接收UDP数据, 与 recv() 类似, 但返回值是(data, address)
                            data ==> 包含接收数据的字符串
                            address ==> 发送端的socket地址
                sendto(str, address): 发送UDP数据, address为元组, 存储接收端的ip与port, 返回发送的字节数
                close(): 关闭套接字
                getpeername(): 返回连接套接字的远程地址, 返回值通常是元组(ipaddr, port)
                getsockname(): 返回套接字自己的地址, 通常是一个元组(ipaddr, port)
                setsockopt(level, optname, value): 设置给定套接字选项的值
                    设置端口复用:
                        socket_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
                            SOL_SOCKET => 打开socket选项列表
                            SO_REUSEADDR ==> 打开端口复用选项
                            True ==> 开启socket选项, 默认为False, 不开启选项
                getsockopt(level,optname[.buflen]): 返回套接字选项的值
                settimeout(timeout): 设置套接字操作的超时期, timeout是一个浮点数, 单位是秒,
                                     值为None表示没有超时期(默认设置)
                gettimeout(): 获取当前套接字设置的超时值, 单位为秒, 如果没有设置, 则返回None
                fileno(): 返回套接字的文件描述符
                setblocking(flag): 如果flag为0, 则将套接字设为非阻塞模式, 否则将套接字设为阻塞模式(默认值)
                                   非阻塞模式下, 如果调用recv()没有发现任何数据 或 send()调用无法立即发送
                                   数据, 那么将引起socket.error异常
                makefile(): 创建一个与该套接字相关连的文件
"""
