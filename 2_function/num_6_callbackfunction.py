"""
    回调函数:
        指函数形参也是一个函数的函数
    定义函数1
        def func1:
            函数代码块
    定义回调函数:
        def func2(func):
            func()
            函数代码块
"""


# 定义函数1
def func1():
    print('我是函数1')


# 定义带有一个形参为函数的回调函数
def func2(func):
    func()
    print('我是函数2')


if __name__ == '__main__':
    # 调用回调函数
    func2(func1)
