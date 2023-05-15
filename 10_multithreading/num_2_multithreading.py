"""
    线程:
        是执行代码(资源)的最小单位, 线程必须依附与进程存在, 每个进程至少有一个线程, 通常为主线程
        多线程与多进程一样可以完成多任务, 线程的执行需要通过CPU调度来完成
    threading ==> python实现多线程的模块
    threading模块使用:
        1. import threading ==> 导入threading模块
        2. child_thread_name = threading.Thread(target=func_name, 传参方式=参数序列)
            两种传参方式:
                a. args ==> 指定以元组方式传入函数参数, 若只有一个参数, 则参数后必须有逗号
                b. kwargs ==> 指定以字典方式传入函数参数, 字典的key必须与形参名完全一致
        3. child_thread_name.start() ==> 开启子线程
    多线程特点:
        1.线程之间执行是无序的
        2.线程之间共享全局变量:
            同一进程的线程使用资源空间相同(同一CPU), 因此可以共享全局变量
            不同进程的线程不在统一资源空间, 无法共享全局变量
        3.主线程会等待所有子线程执行结束再结束
        4.线程之间共享全局变量数据可能会出现错误:
            可能存在同一时刻多个线程操作相同资源数据, 导致结果与预期不符
    守护主线程:
        指让子线程随主线程结束一起结束, 不让主线程再等待子线程执行;
        默认情况下, 主线程会等待子线程结束后再结束
        设置守护主线程两种方式:
            1. 创建子线程时设置参数值 daemon=True:
                child_thread_name = threading.Thread(target=任务名, daemon=True, 传参方式=参数序列)
            2. child_thread_name.setDaemon(True)
    线程池:
        一次性开辟多个线程, 用户直接给线程池提交任务, 线程任务的调度交给线程池完成
        导入线程池:
            from concurrent.futures import ThreadPoolExecutor
        使用线程池:
            1. 创建进程池对象:
                pool_object = ThreadPoolExecutor(pool_num)
                pool_num ==> 线程池中可创建进程个数
            2. 使用线程池对象开启多线程:
                pool_object.submit(func_name, *args / **kwargs)
                可以使用with上下文管理器使用进程池, 并通过循环开启多个进程
                with ThreadPoolExecutor(pool_num) as pool_object:
                    for num in range(pool_num):
                        pool_object.submit(func_name, *args / **kwargs)
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor


def dance(num1: int):
    print('跳舞..', num1)
    time.sleep(1)


def sing(num2: int):
    print('唱歌..', num2)
    time.sleep(1)


if __name__ == '__main__':
    # 创建子线程
    my_dance = threading.Thread(target=dance, args=(5,))  # 以元组形式传参
    my_sing = threading.Thread(target=sing, kwargs={'num2': 5})  # 以字典形式传参
    # 开启子线程
    my_dance.start()
    my_sing.start()
    # 使用线程池执行任务
    with ThreadPoolExecutor(10) as thread_pool:
        for num in range(10):
            if num % 2 == 0:
                thread_pool.submit(sing, num)
            else:
                thread_pool.submit(dance, num)
