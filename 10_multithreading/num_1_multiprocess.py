"""
    进程:
        一个正在"运行"的程序或者软件就是一个进程, 进程是操作系统进行资源分配的基本单位
        一个程序运行后至少有一个进程, 被称为主进程
    多任务:
        指在同一时间执行多个任务, 例如现在的电脑安装的都是多任务操作系统
        优点/目的：充分利用CPU资源,提高程序的执行效率
        多任务实现方式:
            1. 并发执行: 在一段时间内交替去执行多个任务(单核CPU)
            2. 并行执行: 多个CPU内核同一时刻一起执行任务, 始终有多个软件一起执行
    多进程:
        python中实现多任务的一种方式
    multiprocessing ==> python中用来实现多进程的包
    多进程实现:
        1. 导入 multiprocessing包:
            import multiprocessing
        2. 使用Process进程类创建子进程对象
            subprocess_name = multiprocessing.Process(target=func_name, 传参方式=参数序列)
        3. 开启子进程 ==> start()方法:
            subprocess_name.start()
    Process 进程类:
        Process([group[,target[,name[,args[,kwargs]]]]])
        group: 指定进程组, 目前只能使用None
        target: 执行的任务名, 即函数名
        name: 进程名字
        args: 指定以元组方式传入函数参数, 若只有一个参数, 则参数后必须有逗号
        kwargs: 指定以字典方式传入函数参数, 字典的key必须与形参名完全一致
        常用方法:
            start(): 开启子进程
            join(): 等待子进程执行结束后程序再继续向下执行
            terminate(): 立即终止子进程, 不管子进程是否结束
        常用属性: name ==> 当前进程的别名, 默认为Process-N, N为从1开始递增的整数
    获取进程编号:
        目的: 验证子进程与主进程的关系, 可得知子进程是由那个主进程创建的, 子进程需要主进程回收资源
        1. 获取当前进程编号: os.getpid()
        2. 获取父进程编号: os.getppid()
    进程之间不共享全局变量:
        进程是操作系统进行资源分配的基本单位, 创建子进程会对主进程资源进行拷贝,
        子进程相当于主进程的一个副本, 进程之间不共享全局变量(无论是主进程还是子进程),
        是因为操作的不是同一进程的全局变量, 不同进程的全局变量只是名字相同而已
    守护主进程:
        指让子进程随主进程结束一起结束, 不让主进程再等待子进程执行;
        默认情况下, 主进程会等待子进程结束后再结束
        设置守护主进程两种方式:
            1. subprocess_name.daemon = True:
                该方式需要在开启子进程(执行start())之前设置, 否则无效
            2. subprocess_name.terminate(): 销毁子进程, 主进程结束后提前结束子进程
    进程池:
        一次性开辟多个进程, 用户直接给进程池提交任务, 进程任务的调度交给进程池完成
        导入进程池:
            from concurrent.futures import ProcessPoolExecutor
        使用进程池:
            1. 创建进程池对象:
                pool_object = ProcessPoolExecutor(pool_num)
                pool_num ==> 进程池中可创建进程个数
            2. 使用进程池对象开启多进程:
                pool_object.submit(func_name, *args / **kwargs)
                可以使用with上下文管理器使用进程池, 并通过循环开启多个进程
                with ProcessPoolExecutor(pool_num) as pool_object:
                    for num in range(pool_num):
                        pool_object.submit(func_name, *args / **kwargs)
"""
import multiprocessing
import time
import os


def dance(count):
    # 获取子进程ID
    print(os.getpid())
    # 获取父进程ID
    print(os.getppid())
    for i in range(count):
        time.sleep(1)
        print('跳舞...', i)


def sing(num):
    print(os.getpid())
    print(os.getppid())
    for i in range(num):
        time.sleep(1)
        print('唱歌...', i)


if __name__ == '__main__':
    # 获取主进程进程编号
    main_num = os.getpid()
    print(main_num)
    # 使用多进程
    # 创建子进程
    my_dance = multiprocessing.Process(target=dance, args=(5,))  # args传参方式
    my_sing = multiprocessing.Process(target=sing, kwargs={'num': 5})  # kwargs传参方式
    time1 = time.time()
    # 开启子进程
    my_dance.start()
    my_sing.start()
    time2 = time.time()
    print(time2 - time1)
