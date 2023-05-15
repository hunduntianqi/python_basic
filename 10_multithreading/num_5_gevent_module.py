"""
    gevent模块使用:
        1. 将程序执行方式修改为协程运行 ==> 由同步操作改为异步操作
            from gevent import monkey
            monkey.patch_all() ==> 将程序修改为异步执行
        2. 导入gevent包 ==> import gevent
        3. 创建存储任务对象的列表 ==> tasks_list = []
        4. 定义任务函数
        5. 创建任务对象并添加任务对象到任务列表 ==> task = gevent.spawn(任务函数, 函数参数)
            ==> tasks_list.append(task)
        6. 执行所有任务 ==> gevent.joinall(tasks_list)
        queue ==> 队列模块:
            一种有序的数据结构, 可用来存取数据
            1. 导入Queue类 ==> from gevent.queue import Queue
            2. 创建队列对象 ==> queue_name = Queue(num)
                num ==> 队列中可存储数据的最大个数, 可省略, 代表不限制存储数据数量
            队列对象常用方法:
                a. 队列添加数据 ==> queue_name.put_nowait(data)
                b. 从队列中取出数据 ==> queue_name.get_nowait()
                c. 判断队列是否为空 ==> queue_name.empty()
                d. 判断队列是否存满数据 ==> queue_name.full()
                e. 获取队列中剩余数据数量 ==> queue_name.qsize()
        队列模块queue结合gevent任务对象:
            1. 创建Queue()对象, 将需要操作的基本数据存入队列
            2. 创建任务函数, 在任务函数中操作队列取出数据处理
            3. 创建gevent任务对象和任务列表, 将任务对象存入任务列表
            4. 执行所有任务对象
            通过队列将所有基本数据存储起来, 每个任务对象调用任务函数从队列中取出数据操作, 实现在操作
            大量数据时, 每个任务对象内部也是异步操作, 而不是在基本数据过多时, 每个任务对象平分基本数据
            操作, 导致任务对象之间异步, 而在任务对象调用的任务函数内部依然是同步操作的问题
"""
# 从gevent库里导入monkey模块
from gevent import monkey

# monkey.patch_all()能把程序变成协作式运行, 就是可以帮助程序实现异步
monkey.patch_all()
# 导入gevent、time、requests
import gevent, time, requests
# 从gevent库里导入queue模块
from gevent.queue import Queue


# 定义任务函数, 处理数据
def task_func(work: Queue):
    # work.empty() ==> 判断队列是否为空, 用作循环判断条件
    while not work.empty():
        # 从队列中取出数据
        data = work.get_nowait()
        # 访问网站
        # response = requests.get(data)
        # 返回队列中剩余数据数量
        num = work.qsize()
        # 打印从队列中取出的数据
        # print("队列中获取数据为: {}; 网站状态码为:{}; 队列中剩余数据数量为{}".format(
        #     data, response.status_code, num))
        print("队列中获取数据为: {}; 队列中剩余数据数量为{}".format(data, num))


if __name__ == '__main__':
    # 记录程序开始时间
    start = time.time()
    # 定义列表存储基本数据
    url_list = ['https://www.baidu.com/',
                'https://www.sina.com.cn/',
                'http://www.sohu.com/',
                'https://www.qq.com/',
                'https://www.163.com/',
                'http://www.iqiyi.com/',
                'https://www.tmall.com/',
                'http://www.ifeng.com/']
    # 创建队列对象
    work = Queue()
    for url in url_list:
        # 遍历url_list, 将列表中的数据入队列
        work.put_nowait(url)

    # 定义列表存储任务对象
    task_list = []
    # 创建三个任务对象并存入任务列表
    for i in range(8):
        # 创建任务对象
        task = gevent.spawn(task_func, work)
        # 任务对象添加列表
        task_list.append(task)
    # 执行所有任务
    gevent.joinall(task_list)
    # 记录结束时间
    end = time.time()
    print("程序运行共耗时为:{}s".format(end - start))
