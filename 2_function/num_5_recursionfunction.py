"""
    递归函数:
        函数定义后, 在函数内部直接或间接的调用自己
"""


# 定义递归函数
def sum_digui(num: int):
    if num == 1:
        return num
    return num * sum_digui(num - 1)


if __name__ == '__main__':
    # 调用递归函数累加数据
    # num = sum_digui(100)
    print(sum_digui(995))
