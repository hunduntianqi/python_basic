"""
    os模块:
        系统操作相关模块
"""
import os

# os.getcwd() 获取当前工作目录路径
print(os.getcwd())  # D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块

# os.chdir() 修改当前目录为指定路径
os.chdir(r'D:\Users\Administrator\Desktop\小练习\test\go_图片备份')
print(os.getcwd())

# os.listdir() 获取指定目录或当前目录下的文件名列表
print(os.listdir())  # 获取当前目录下的文件名列表
print(os.listdir(r'D:\Users\Administrator\Desktop\小练习'))  # 获取指定目录下的文件名列表

# os.mkdir(文件夹路径, 权限(仅限linux)) 在指定位置创建指定名称的文件夹
# os.mkdir('./os模块练习') # 当文件夹已存在时, 再次执行代码会报错

# os.makedirs() 可以递归创建文件夹
os.chdir(r'D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块')
# os.makedirs('./递归创建文件夹/文件夹1/文件夹2')  # 当文件夹已存在时, 再次执行代码会报错

# os.rmdir() 删除空文件夹
# os.rmdir('./递归创建文件夹/')

# os.removedirs() 递归删除空文件夹
# os.removedirs(r'D:\Users\Administrator\IdeaProjects\py_Study\2_内置模块\递归创建文件夹\文件夹1\文件夹2')

# os.remove() 删除文件
# os.rename() 修改文件或文件夹的名字

# os.system() 执行操作系统中的命令
