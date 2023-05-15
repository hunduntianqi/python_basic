"""
    类属性:
        属于类的特征, 可以用类名直接访问
        定义类属性
        class class_name:
            class_property_name : type
            实例方法
            类方法
            静态方法
    python类中的三种方法:
        实例方法:
            def method_name(self):
                pass
            特点: 至少包含一个 self 参数, 由类的对象调用, 属于对象的行为特征
        类方法:
            @classmethod
            def method_name(cls):
                pass
            特点: 使用 @classmethod 进行标记, 最少也要包含一个参数, 用来指代类, 一般为cls
            类方法调用: 使用类名调用(推荐), 使用对象调用(不推荐)
        静态方法:
            @staticmethod
            def method_name():
                pass
            特点: 使用 @staticmethod 进行标记, 无特殊参数, 无法调用类属性和类方法, 无self参数, 也无法调用对象相关内容
            静态方法调用: 可以使用类名调用, 也可以使用类对象调用, 与普通的函数类似
"""


# 定义Test类
class Test:
    # 定义类属性count, 记录创建的对象个数
    count: int = 0

    # 定义实例方法
    def __init__(self):
        Test.count += 1  # 使用类名调用类属性
        print('__init__是一个实例方法, 在创建对象时自动调用')

    # 定义类方法
    @classmethod
    def class_method(cls):
        print('我是一个类方法, 可以由类名直接调用, 是属于类的')

    # 定义静态方法
    @staticmethod
    def static_method(name: str):
        print('我是一个静态方法, 我是{}'.format(name))


if __name__ == '__main__':
    # 创建三个对象
    test = Test()
    test1 = Test()
    test2 = Test()
    print(type(test), type(test1), type(test2))
    # 类名访问类属性
    print("当前创建的测试类对象个数为: {}".format(Test.count))
    # 类名调用类方法
    Test.class_method()
    # 类名调用静态方法
    Test.static_method("郭鹏涛")
    # 对象调用静态方法
    test.static_method("混沌天帝")
    # 对象调用类方法
    test.class_method()
    # 对象访问类属性
    print("当前创建的测试类对象个数为: {}".format(test.count))