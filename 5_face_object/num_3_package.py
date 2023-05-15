"""
    封装:
        面向对象三大特征之一
        告诉我们如何正确设计对象的属性和方法
        原则: 对象代表什么, 就得封装对应的数据, 并提供数据对应的行为
        封装的优点:
            1. 让编程变得简单, 有什么事, 找对象, 调方法就行了
            2. 降低学习成本, 可以少学, 少记, 不需要记对象有哪些方法, 有需要时去找就行了
        封装实现步骤:
            1. 对不希望公开的属性和方法进行私有化处理
            2. 对象通过特定的方式访问私有成员
        私有属性和私有方法定义:
            私有属性 ==> __property_name
            私有方法 ==> __method_name(self, 形参列表)
        访问私有属性和私有方法:
            访问私有属性 ==> object_name._class_name__property_name
            访问私有方法 ==> object_name._class_name__method_name()
"""


class Student:
    def __init__(self, name, age):
        # 定义私有成员变量
        self.__name = name
        self.__age = age

    # 定义私有方法
    def __message(self):
        print("name = {}, age = {}".format(self.__name, self.__age))


if __name__ == '__main__':
    # 创建对象
    student = Student("郭鹏涛", 24)
    # 访问私有成员变量
    print(student._Student__name)
    print(student._Student__age)
    # 访问私有方法
    student._Student__message()
