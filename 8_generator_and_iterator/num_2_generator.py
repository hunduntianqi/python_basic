"""
    生成器:
        在 Python 中, 使用了 yield 的函数被称为生成器
        生成器是一个返回迭代器的函数, 只能用于迭代操作, 或者说生成器就是一个迭代器
        在调用生成器运行的过程中, 每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值,
        并在下一次执行 next() 方法时从当前位置继续运行
        调用一个生成器函数，返回的是一个迭代器对象
        定义生成器函数:
            def func_name(variable_name):
                操作代码
                yield generator_variable_name
                其他操作代码(不一定有)
        列表推导式定义生成器:
            generator_name = (variable_name for variable_name in iterator_object if 判断条件(可省略))
        生成器元素迭代:
            格式一: generator_name.__next__()
            格式二: next(generator_name)
"""


def generator_feibonaqi(num: int):
    a, b, count = 1, 0, 0
    while True:
        yield a
        a, b = a + b, a
        count += 1
        if count > num:
            return


if __name__ == '__main__':
    # 利用生成器产生斐波那契数列
    f = generator_feibonaqi(10)
    print(type(f))
    for num in f:
        print(num)

    # 列表推导式产生生成器
    list_generator = (num for num in range(10))
    print(type(list_generator))
    print(list_generator.__next__())
    print(next(list_generator))
    print(next(list_generator))
    print(next(list_generator))
    print(next(list_generator))
    print(next(list_generator))
    print(next(list_generator))
    print(next(list_generator))
    print(next(list_generator))
    print(next(list_generator))
    print(next(list_generator))
