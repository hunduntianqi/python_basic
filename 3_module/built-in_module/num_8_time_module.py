"""
    time模块:
"""

import time

# 获取当前系统的时间戳 time.time(); 时间戳: 表示从1970年1月1日0时0分0秒到当前时刻的秒数
print(time.time())

# 获取系统当前时间, 时间字符串 time.ctime()
print(time.ctime())

# 获取当前系统时间 时间元组
print(time.localtime())

# strftime() 格式化时间 年-月-日 时:分:秒 星期几
print(time.strftime('%Y-%m-%d %H:%M:%S %w'))

# time.sleep() 等待指定时间后再继续运行
time.sleep(3)  # 程序等待三秒

# 计算程序的运行时间 time.perf_counter()
print(time.perf_counter())
