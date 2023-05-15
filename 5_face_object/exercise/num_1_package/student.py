# 定义学生类
class Student:
    # 定义类的初始化方法(用来创建对象)
    def __init__(self, name: str = None, age: int = None, sex: str = None):
        # 定义类的私有成员变量(成员属性)
        self.__name: str = name
        self.__age: int = age
        self.__sex: str = sex

    # 定义类的私有成员方法
    def __secret(self):
        print("每个学生都有自己的小秘密~~~")

    # 定义类的公共方法
    def study(self):
        print("每个学生都应该好好学习!!")

    """
        模仿Java, 定义set&get方法
    """

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age: int):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_sex(self, sex: str):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    # 重写str方法
    def __str__(self):
        return "name: {} age: {} sex: {}".format(self.__name, self.__age, self.__sex)
