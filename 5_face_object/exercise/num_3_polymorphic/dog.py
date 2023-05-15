"""
    定义一个Dog类, 继承自Animal类
"""
from Animal import Animal


class Dog(Animal):
    # 定义狗类, 具有看家的行为
    def look_door(self):
        print("{} 在看家~~".format(super().get_name()))

    # 重写eat()方法
    def eat(self):
        super().eat()
        print("{} 在吃骨头~~~".format(super().get_name()))
