"""
    定义学生类, 封装学生信息
        学号, 姓名, 年龄, 分数
"""


class Student:

    # 定义初始化方法, 定义实例属性
    def __init__(self, id_num: int = None, name: str = None, age: int = None, score: float = None):
        self.__id_num = id_num
        self.__name = name
        self.__age = age
        self.__score = score

    # 定义get(), set()方法
    def set_id_num(self, id_num: int):
        self.__id_num = id_num

    def get_id_num(self):
        return self.__id_num

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age: int):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_score(self, score: float):
        self.__score = score

    def get_score(self):
        return self.__score

    # 重写str方法
    def __str__(self):
        return "Student[id_num: {}, name: {}, age: {}, score: {}]".format(self.__id_num, self.__name,
                                                                          self.__age, self.__score)
