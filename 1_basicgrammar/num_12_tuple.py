"""
    元组 == tuple:
        与列表类似, 但元组中的元素不能修改
        1）元组表示多个元素组成的序列, 在Python开发中,有特定的应用场景
        2）专门用于存储一串信息
        3）元组用 () 定义, 数据之间用英文逗号 , 分隔
        4）元组的索引从 0 开始
        注意: 当元组中只包含一个元素时, 需要在元素后面加 ','; 例: tuple(data,)
        常用方法:
            1. tuple.index(data): 取元组中对应数据的索引值
            2. tuple.count(data): 统计数据在元祖中出现的次数
        元组转换为列表 ==> list(tuple_name)
"""


# 定义函数, 嵌套元组遍历
def tuple_ergodic(tuple_name: tuple):
    for name in tuple_name:
        if isinstance(name, tuple):
            tuple_ergodic(name)
        else:
            print(name, end="  ")


if __name__ == '__main__':
    # 定义嵌套元组
    tuple_name: tuple = (1, 2, 3, (4, 5, 6, ('*', 6, 5, 9, 11)))
    # 调用函数, 遍历元组
    tuple_ergodic(tuple_name)
