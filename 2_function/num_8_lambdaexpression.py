"""
    匿名函数-lambda表达式:
    匿名函数:
        可以不使用def定义且无函数名的函数
        在python中使用lambda表达式定义匿名函数
        注意:
            lambda表达式仅仅是一个表达式, 不是代码块, 所以lambda表达式只能写在一行代码
            lambda表达式也有形参, 并且不能访问除了自己的形参之外的任何数据(包括全局变量)
        语法格式:
            lambda [参数列表] : 返回值
        带有分支结构的lambda表达式
            lambda 参数列表: 条件为真返回值 if 判断条件 else 条件不为真返回指
"""
if __name__ == '__main__':
    # lambda做加法运算
    lambda_sum = lambda x, y: x + y
    print(lambda_sum(1, 5))

    lambda_max = lambda x, y: x if x > y else y
    print(lambda_max(1, 3))

