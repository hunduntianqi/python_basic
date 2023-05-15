"""
    os.path: 系统中的路径模块
"""

import os

# os.path.abspath(相对路径) 将相对路径转换为绝对路径
print(os.path.abspath('/'))  # D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块

# 获取路径中的主体部分
print(os.path.basename(r'D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块'))  # 2_内置模块

# 获取路径中的路径部分
print(os.path.dirname(
    r'D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块'))  # D:\Users\Administrator\IdeaProjects\py_Study

# join() 连接多个路径, 组成一个新的路径
print(os.path.join('./12/3/', './5.jpg'))

# split() 拆分路径, 把路径拆分为路径和主体部分
print(os.path.split(r"D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块"))

# splitext() 拆分路径, 可以拆分文件后缀名
print(os.path.splitext(r'D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块\3_随机模块_random.py'))

# 获取文件大小
print(os.path.getsize(r'D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块\3_随机模块_random.py'))

# 检测是否是一个文件夹
print(os.path.isdir(r'D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块\3_随机模块_random.py'))

# 检测文件是否存在
print(os.path.isfile('./1_序列化_pickle.py'))

# 检测路径是否存在
print(os.path.exists('./1_序列化_pickle.py'))

# 检测两个路径是否同时指向一个目标位置
print(os.path.samefile('./1_序列化_pickle.py', './2_数学模块_Math.py'))
