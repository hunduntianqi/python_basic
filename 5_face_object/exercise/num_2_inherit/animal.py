"""
    定义一个动物类
"""


class Animal:
    def __init__(self, name: str = None):
        # 属性 ==> name
        self.__name = name

    # 定义方法, 吃东西
    def eat(self):
        print("{} 在吃饭~~".format(self.__name))

    # 定义方法, 喝水
    def drinking(self):
        print("{} 在喝水~~".format(self.__name))

    # 定义get()&set()方法
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
