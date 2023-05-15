"""
    删除文件夹, 考虑子文件夹
"""
import os


# 定义函数, 删除文件夹
def del_dir(dir_path: str):
    # 1. 获取文件夹下所有文件名
    file_name_list: list = os.listdir(dir_path)
    # 2. 拼接文件路径
    for file_name in file_name_list:
        file_path = dir_path + "\\" + file_name
        # 判断是否为文件夹
        if os.path.isdir(file_path):
            # 判断是否为空文件夹
            if len(os.listdir(file_path)) == 0:
                # 空文件夹, 直接删除
                os.rmdir(file_path)
            else:
                # 不是空文件夹, 递归删除文件夹内文件
                del_dir(file_path)
        else:
            # 不是文件夹, 删除文件
            os.remove(file_path)
    else:
        # 判断传入参数指向文件夹是否存在, 存在则删除
        if os.path.exists(dir_path):
            os.rmdir(dir_path)


if __name__ == '__main__':
    dir_path = input("请输入要删除文件夹路径:")
    # 调用函数, 删除文件夹内所有数据
    del_dir(dir_path)
    # # 删除源文件夹
    # os.rmdir(dir_path)
    print("文件夹已删除!!")
    pass
