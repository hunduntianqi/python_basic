"""
    定义一个Cat类, 继承自Animal类
"""
from Animal import Animal


class Cat(Animal):
    # 定义狗类, 具有看家的行为
    def grab_mouse(self):
        print("{} 在抓老鼠~~".format(super().get_name()))
