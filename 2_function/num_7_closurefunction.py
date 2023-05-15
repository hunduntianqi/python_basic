"""
    闭包函数:
        1. 在一个函数内部返回了一个内函数
        2. 内函数中使用了外部函数中的局部变量
        3. 返回的内函数就是闭包函数
        def outer():
            num = 0
            def inner():
                nonlocal num
                num = 5
            return inner
        闭包的作用: 保护了函数中的局部变量不受外部影响, 但是又可以正常使用
        闭包函数检测:
            函数名.__closure__:
                如果是闭包函数,返回cell, 不是返回None
"""


class Test(object):
    # 定义闭包函数
    def outer(self):
        num = 0

        def inner():
            nonlocal num
            num += 5
            print(num)

        # inner()
        return inner  # 在外函数中返回了内函数, 内函数就是闭包函数


if __name__ == '__main__':
    # 创建对象
    test = Test()
    # 调用闭包函数
    number = test.outer()
    number()  # 局部变量num ==> 5
    number()  # 局部变量num ==> 10
    number()  # 局部变量num ==> 15
    print(test.outer.__closure__)
    print(number.__closure__)
