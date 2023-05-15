"""
    zipfile模块:
        数据压缩与归档, 该模块提供了用于创建, 读取, 写入,附加和列出zip文件的工具
"""

import zipfile

# zipfile.ZipFile(路径包名, 模式(r, w, a), 压缩或打包)
# 压缩文件
with zipfile.ZipFile('./1_序列化_pickle', 'w') as myzip:
    myzip.write('./1_序列化_pickle.py')  # 向压缩包写入要压缩的文件

# 解压缩文件
with zipfile.ZipFile('./1_序列化_pickle', 'r') as myzip:
    myzip.extractall('./')
