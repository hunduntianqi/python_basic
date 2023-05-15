"""
    定义Person抽象类
"""
from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self, name: str = None, age: int = None):
        self.__name = name
        self.__age = age

    # 定义抽象方法
    @abstractmethod
    def work(self):
        pass

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age: int):
        self.__age = age

    def get_age(self):
        return self.__age

    # 重写__str__方法
    def __str__(self):
        return "name: {}; age: {}".format(self.__name, self.__age)
