"""
    定义学生类继承Person类, 并重写抽象方法
"""
from Person import Person


class Student(Person):
    # 重写抽象方法
    def work(self):
        print("学生{}的工作是好好学习!!".format(super().get_name()))
