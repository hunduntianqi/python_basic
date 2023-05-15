"""
    input()函数:
        python中用来接收键盘输入信息的函数
        格式:
            variable_name = input('提示信息(可不填)')
            注意: input() 函数接收数据后返回值为str类型, 如果需要其他数据, 需要强制转换类型
"""

# 使用input函数接收数字
num = int(input('请输入一个整数:\n'))  # 强制转换类型将str数据转换为int数据
print(num)
print(type(num))  # <class 'int'>
