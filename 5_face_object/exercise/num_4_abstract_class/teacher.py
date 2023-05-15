"""
    定义老师继承Person类, 并重写抽象方法
"""
from Person import Person


class Teacher(Person):
    def work(self):
        print("教师{}的工作是教书育人".format(super().get_name()))
