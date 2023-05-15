"""
    asyncio模块使用:
        Python3.4中引入的模块, 用于编写协程代码
        async & await: 在Python3.5中引入的两个关键字, 结合asyncio模块可以更方便的编写协程代码
        事件循环:
            类似一个while循环, 在周期性的运行并执行一些任务, 在特定条件下终止循环
            获取事件循环 ==> event_loop = asyncio.get_event_loop()
        协程函数:
            使用 'async' 关键字修饰定义的函数:
                async def func_name():
                    pass
        协程对象:
            调用协程函数返回的对象:
                object_name = func_name()
                注意: 调用协程函数时, 函数内部代码不会执行, 只是会返回一个协程对象
        执行协程函数:
            方式一:
                a. 创建事件循环 ==> event_loop = asyncio.get_event_loop()
                b. 执行协程任务 ==> loop.run_until_complete(object_name)
            方式二: asyncio.run(object_name)
            执行原理:
                将协程对象当做一个任务添加到事件循环的任务列表, 事件循环检测任务列表中的协程
                是否准备就绪(默认准备就绪), 如果准备就绪则执行其内部代码
        await:
            一个只能在协程函数中使用的关键字
            作用: 在程序遇到IO操作时, 挂起当前协程, 使得事件循环可以先去执行其他协程任务,
                  当IO操作完成时, 再将事件循环切换回来继续执行该协程代码
            使用方式:
                在协程函数中 ==> await io操作代码
        Task对象:
            用于并发调度协程, 本质上是将协程对象封装成task对象, 并将协程立即加入事件循环, 同时追踪协程的状态
            创建Task对象三种方式:
                1. task_name = asyncio.create_task(协程对象) [python 3.7新加入]
                2. task_name = loop.create_task(协程对象)
                3. task_name = ensure_future(协程对象)
                执行任务对象: await task_name
                注意: 若任务对象封装函数有返回值, 需要使用变量来接收返回值
        asyncio.wait(task_list):
            1. 将列表封装为一个协程
            2. 源码内部对列表中的每个协程执行ensure_future封装为Task对象
            loop.run_until_complete(asyncio.wait(task_list)) == > 执行协程任务
        异步上下文管理器:
            async with 调用函数 as 函数别名:
                pass
        在程序中只要看到async和await关键字, 其内部就是基于协程实现的异步编程, 这种异步编程是通过一个线程
        在IO等待时间去执行其他任务, 从而实现并发
        uvloop模块:
            属于第三方模块, 可以替换asyncio中的事件循环方案, 提高asyncio模块的执行性能
            安装模块: pip install uvloop
            使用uvloop替换asyncio的事件循环:
                asyncio.set_event_loop_policy(uvloop.EventLoopPolicy()) ==> 内部的事件循环自动化会变为uvloop
            其他代码使用不变
            uvloop模块目前不支持Windows系统
"""
# 导入asyncio模块
import asyncio
import time


# 定义协程函数
async def func_name(num: int):
    print('协程-{}开始执行'.format(num))
    await asyncio.sleep(10)
    print('协程-{}执行结束'.format(num))


if __name__ == '__main__':
    start_time = time.time()
    # 根据列表推导式生成列表
    list_num: list[int] = [num for num in range(100000)]
    # 循环生成协程对象列表
    object_list: list = [func_name(num) for num in list_num]
    # 创建事件循环
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.wait(object_list))
    end_time = time.time()
    print('共耗时:{}s'.format(end_time - start_time))
