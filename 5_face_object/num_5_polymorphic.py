"""
    多态:
        面向对象三大特征之一
        指完成某个行为, 使用不同的对象, 会得到不同的状态
        多态的前提:
            有继承和方法重写
    抽象类(接口):
        使用 abc 模块可以很轻松的定义抽象基类
        使用方法:
            a. 导入abc模块:
                from abc import ABCMeta, abstractmethod
            b. 定义抽象类:
                class class_name(metaclass=ABCMeta):
                    # 定义抽象方法
                    @abstractmethod
                    def method_name(self, param_name: type):
                        pass
        抽象类不能被实例化, 抽象类的目的就是让别的类继承它并实现特定的抽象方法
"""
from abc import ABCMeta, abstractmethod


# 定义Animal抽象类
class Animal(metaclass=ABCMeta):
    # 定义抽象方法eat
    @abstractmethod
    def eat(self):
        pass

    # 定义抽象方法run()
    @abstractmethod
    def run(self):
        pass


# 定义Dog类, 继承Animal类
class Dog(Animal):
    # 重写eat()方法
    def eat(self):
        print('狗吃骨头')

    # 重写run()方法
    def run(self):
        print("狗跑得很快")


# 定义Cat类, 继承Animal类
class Cat(Animal):
    # 重写eat()方法
    def eat(self):
        print('猫吃鱼')

    # 重写run()方法
    def run(self):
        print("猫跑得也很快")


if __name__ == '__main__':
    # 创建Dog对象
    dog = Dog()  # type: Animal
    # 创建Cat对象
    cat = Cat()  # type: Animal
    dog.eat()
    dog.run()
    cat.eat()
    cat.run()
