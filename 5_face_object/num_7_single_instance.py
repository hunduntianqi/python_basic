"""
    单例设计模式:
        目的: 让类创建的对象, 在系统中只有一个唯一的实例, 每次调用 class_name() 返回的对象, 在内存中地址是相同的
        __new__方法:
            是一个由object基类提供的内置的静态方法
            a. 在内存中为对象分配空间
            b. 返回对象的引用 ==> 地址值
        创建对象时, 当python解释器获得__new__方法返回的对象引用时, 会将其作为第一个参数传递给__init__方法
        单例设计模式实现步骤:
            1. 定义类属性, 记录对象引用
            2. 重写__new__方法, 判断对象引用是否为None, 是 ==> return super().__new__(cls) ==> 为对象分配空间
                不是 ==> return 对象引用
        让初始化方法__init__执行一次:
            1. 定义类属性 flag, 类型为 bool, 用来判断初始化方法是否被执行过
            2. 若初始化方法未被执行, 则执行初始化方法, 并修改 flag 的值, 执行过初始化方法, 直接return结束
"""


# 定义测试类, 演示单例模式
class Test:
    # 创建类属性, 记录对象引用
    instance_id = None
    # 创建类属性, 记录初始化方法是否被执行过
    init_flag: bool = False

    # 重写__new__方法
    def __new__(cls, *args, **kwargs):
        # 判断对象是否被创建过
        if cls.instance_id == None:
            # 未创建对象, 为对象分配内存, 创建对象并返回对象引用
            cls.instance_id = super().__new__(cls)
            return cls.instance_id
        else:
            # 对象已创建, 直接返回对象引用
            return cls.instance_id

    def __init__(self):
        if not Test.init_flag:
            print('执行初始化')
            Test.init_flag = True
        else:
            print('不再执行初始化')


if __name__ == '__main__':
    # 创建多个测试类对象, 打印id看地址是否一致
    test1 = Test()
    test2 = Test()
    test3 = Test()
    print(id(test1))
    print(id(test2))
    print(id(test3))
