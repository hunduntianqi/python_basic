"""
    程序执行结构:
        1. 顺序执行: 程序从上至下, 顺序执行
        2. 分支机构: 根据不同的条件结果, 选择不同的代码执行
        3. 循环结构: 重复执行相同代码
    循环语句:
        break: 直接结束当前所在循环体的执行, 只能结束当前循环, 若存在循环嵌套, 内层循环的break不能结束外层循环
        continue: 结束本轮循环, 直接进入下次循环
        pass: 是空语句, 一般用作占位语句, 不做任何事情
        for 循环:
            语法格式:
                for 遍历变量 in 可迭代数据:
                    循环体
                for 循环通过可迭代数据来控制循环次数, 也可以使用break关键字结束循环, 或使用
                continue关键字跳过本次循环进入下一轮循环
        while 循环:
            语法格式:
                while bool值为真的数值或表达式:
                    循环体
                while 循环需要设置循环条件, 并且在不断循环中会修改该条件, 否则可能导致死循环
                while循环也可以使用break关键字结束循环, 或使用continue关键字跳过本次循环
    for-in-else / while-else 结构 ==> 在执行完循环正常结束后, 会执行else后的代码(被break中断循环则不执行else的代码)
"""


# 循环打印正方形
def print_square():
    for i in range(5):
        print('* * * * * * *')
    else:
        print("正方形打印结束!!")


# 打印三角形
def print_delta():
    for i in range(6):
        print("* " * (i + 1))
    else:
        print("三角形打印结束!!")


# 打印九九乘法表
def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} * {} = {}\t'.format(j, i, j * i), end="")
        print()
    else:
        print("九九乘法表打印结束!!")


if __name__ == '__main__':
    print('打印正方形:')
    print_square()
    print("========================")
    print("打印三角形:")
    print_delta()
    print("========================")
    print("打印九九乘法表:")
    print_multiplication_table()
