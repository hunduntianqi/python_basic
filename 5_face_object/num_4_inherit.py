"""
    继承:
        面向对象编程三大特性之一
        单继承的语法格式:
            class class_name(parent_class_name):
                子类特有的成员变量
                子类特有的成员方法
        继承的传递性: 子类拥有父类以及父类的父类中封装的所有属性和方法
        注意：继承自同一父类的子类之间,如果没有直接的继承关系, 不能调用其他子类的属性和方法
        方法的重写:
            当父类的方法实现不能满足子类需求时, 可以对父类方法进行重写
            1. 覆盖父类方法:
                父类的方法实现和子类的需求完全不同, 可以在子类中重新编写父类的方法, 相当于在子类中定义了新的方法
            2. 对父类方法进行扩展:
                a. 在子类中重写父类的方法
                b. 在需要的位置使用super().父类方法来调用父类方法的执行
                c. 代码其他位置针对子类的需求,编写子类特有的代码实现
                super:
                    1.在Python中super是一个特殊的类
                    2.super()是使用super类创建的对象
                    3.最常使用的场景就是在重写父类方法时,调用在父类中封装的方法实现
        父类的私有属性和私有方法:
            子类对象不能直接访问父类的私有属性和私有方法, 可以通过父类的公共方法访问私有成员
        多继承语法格式:
            class class_name(parent_class_name1, parent_class_name2, ...):
                子类特有的成员变量
                子类特有的成员方法
        内置属性__mro__:
            主要用于在多继承时判断方法、属性的调用路径; 在搜索方法时, 是按照__mro__的输出结果从左至右的顺序查找的
            多继承中的方法调用顺序遵循就近原则:
                1. 先在本类中寻找, 找到就执行
                2. 然后按照代码编写中继承父类的先后顺序依次寻找对应方法, 找到就执行
                3. 如果在所有的类中均未找到对应方法, 程序报错
            注意: __mro__是属于类的属性, 必须使用类名访问 ==> class_name.__mro__, 返回对象为元组
"""


# 单继承演示
class Phone:
    brand = None  # type: str
    price = None  # type: float

    def __init__(self, brand: str, price: float):
        self.brand = brand
        self.price = price

    def call(self):
        print('4G通话')


# 定义类继承Phone类
class NewPhone(Phone):
    def call(self):
        print('5g通话')

    def __str__(self):
        return 'NewPhone[brand={}, price={}]'.format(self.brand, self.price)


# 定义2022年手机类
class Phone2022(NewPhone, Phone):
    def face_recognition(self):
        print('2022年的新手机 {} 新增人脸识别功能'.format(self.brand))


if __name__ == '__main__':
    # 创建新手机类对象
    new_phone = NewPhone("华为", 1999)
    print(new_phone)
    print(type(NewPhone.__mro__))  # (<class '__main__.NewPhone'>, <class '__main__.Phone'>, <class 'object'>)
    print(Phone2022.__mro__)  # (<class '__main__.Phone2022'>, <class '__main__.NewPhone'>,
    # <class '__main__.Phone'>, <class 'object'>)
    # 创建2022年手机类
    phone_2022 = Phone2022("nova6 5G", 2600)  # type: Phone2022
    phone_2022.face_recognition()
