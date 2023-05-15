"""
    互斥锁:
        解决多线程操作时, 多个线程操作统一资源冲突问题
        原理:
            对共享数据进行锁定, 保证同一时刻只能由一个线程去操作
        互斥锁存在时程序执行流程:
            多个线程一起去抢一个共享数据, 抢到锁的线程先执行, 其他线程需要等待,
            等到互斥锁使用完释放数据后, 其他线程再去抢这个锁
        Lock() ==> threading模块定义的Lock变量, 本质为一个函数, 调用此函数可以获取一个互斥锁对象
        Lock()使用:
            1. 创建互斥锁对象: mutex = threading.Lock()
            2. 给共享数据上锁: mutex.acquire()
            3. 释放锁: mutex = release()
            注意:
                a. acquire()和release()之间的代码为被上锁数据, 同一时刻只能有一个线程操作
                b. 在调用acquire()方法时, 如果其他线程已经使用互斥锁, acquire()方法会被堵塞,
                   直到互斥锁释放后才能再次上锁
"""

import threading

# 定义全局变量
g_num = 0  # type: int
# 创建互斥锁
mutex = threading.Lock()


def sum_num1():
    global g_num
    # 上锁
    mutex.acquire()
    for i in range(10000000):
        g_num += 1
    # 释放锁(不解锁会出现死锁问题...)
    mutex.release()
    print('sum_num1: ', g_num)


def sum_num2():
    global g_num
    mutex.acquire()
    for i in range(10000000):
        g_num += 1
    mutex.release()
    print('sum_num2:', g_num)


if __name__ == '__main__':
    # 创建子线程
    sum1 = threading.Thread(target=sum_num1)
    sum2 = threading.Thread(target=sum_num2)
    # 开启子线程
    sum1.start()
    # sum1.join()  # 等待sum1线程执行完再执行sum2线程
    sum2.start()
