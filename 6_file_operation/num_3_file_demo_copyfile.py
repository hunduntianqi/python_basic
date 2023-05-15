"""
    复制文件夹, 考虑子文件夹
"""
import os


# 定义函数, 获取源文件夹中所有文件路径
def get_source_file_path(path_resource: str) -> list[str]:
    # 1. 创建列表, 存储源文件文件路径
    list_source_path: list[str] = []
    # 2. 获取源文件夹中所有文件名列表
    list_file_name = os.listdir(path_resource)
    for file_name in list_file_name:
        # 3. 拼接文件路径
        file_path = path_resource + "\\" + file_name.lower()
        # 4. 将文件路径添加到列表
        list_source_path.append(file_path)
        # 5. 判断文件对象是否为文件夹
        if os.path.isdir(file_path):
            # 是文件夹, 递归
            list_source_path.extend(get_source_file_path(file_path))
    return list_source_path


# 定义函数, 复制文件
def copy_file(path_source: str, path_result: str, list_source_path: list[str]):
    # 1. 循环遍历存储源文件路径列表
    for source_file_name in list_source_path:
        # 2. 修改源文件路径, 修改源文件夹为目标文件夹
        result_file_path = source_file_name.replace(path_source, path_result)
        # 3. 判断源文件对象是否为文件夹
        if os.path.isdir(source_file_name):
            # 源文件对象是文件夹, 创建文件夹对象
            if os.path.exists(result_file_path):
                print("文件夹已存在")
            else:
                os.mkdir(result_file_path)
        else:
            # 源文件对象为文件, 读取源文件数据, 写入目标文件
            with open(source_file_name, "rb") as file_source:
                # 按行读取源文件数据到列表中
                file_data: list = file_source.readlines()
                # 将数据写入目标文件对象
                with open(result_file_path, "wb") as file_result:
                    for data in file_data:
                        file_result.write(data)
    pass


if __name__ == '__main__':
    path_source: str = input("请输入源文件夹路径:")
    # 调用函数, 获取原文件路径
    source_file_name: list = get_source_file_path(path_source)
    print(source_file_name)
    path_result: str = input("请输入目标文件夹路径:")
    # 创建目标文件夹对象
    if os.path.exists(path_result):
        print("文件夹已存在")
    else:
        os.mkdir(path_result)
    # 调用函数, 复制文件
    copy_file(path_source, path_result, source_file_name)
    print("文件复制完毕!!")
