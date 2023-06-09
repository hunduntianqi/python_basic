"""
    UDP通信协议:
        用户数据报协议, 是一种无连接, 不可靠传输的协议
        特点:
            1. 是一种无连接, 不可靠传输的协议
            2. 将数据源IP, 目的地IP和端口封装成数据包, 不需要建立连接
            3. 每个数据包的大小限制在64KB内
            4. 发送不管对方是否准备好, 接收方收到也不确认, 所以不可靠
            5. 可以广播发送, 发送数据结束时无需释放资源, 开销小, 速度快
        通信场景:
            语音通话, 视频会话等
        在UDP传输协议中, 与连接相关的方法均不支持使用
"""