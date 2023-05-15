"""
    内部函数:
        在函数内部定义的函数
        def outer():
            def inner:
                函数功能代码
            函数功能代码
            return
        注意:
            1. 在函数内部定义的函数在外部无法访问, 只能在外部函数内部调用内部函数
            2. 在内部函数可以访问外部函数的内容, 但不能直接操作外部函数内容
        nonlocal关键字:
            在内部函数中使用nonlocal关键字声明外部函数变量, 可以使内部函数操作外部函数变量, 但变量仍然不是全局变量
"""

if __name__ == '__main__':
    # 定义包含内部函数的函数
    def outer():
        print('this is one outer function')
        num = 0

        def inner():
            # 内部函数无法直接访问外部函数变量, 需要使用nonlocal关键字进行声明
            nonlocal num
            num += 2
            print(num)  # 打印外部函数变量num, 可以获取外部函数变量
            print('this is one inner function')

        inner()  # 调用内部函数 ==> num = 2
        print(num)
        inner()  # 调用内部函数 ==> num = 4
        # print(sum) 外部函数未定义变量在外部函数无法使用


    outer()
    print(globals())
