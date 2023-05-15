"""
    面向对象编程:
        Object Oriented Programming, 简称OOP, 是一种以对象为中心的程序设计思想
        面向对象编程三大特征: 封装, 继承, 多态
        面向对象的核心是对象, 是一个特征和功能的综合体
        优缺点:
            优点: 可扩展性高
            缺点: 变成复杂度相对高
        类: 是对象的一个抽象(模具)
        属性: 对象的特征
        方法: 对象的功能
        实例(对象): 是类的一个实例(由模具打造的器件)

    类的定义:
        通过class关键字定义:
            class 类名:
                类的属性和方法
        类的实例化-创建对象
            对象名 = 类名()
"""
import winsound


class Clock:
    name = None
    id = None

    # 定义方法, 让闹钟响起
    def ring(self):
        winsound.Beep(1000, 5000)

    def __str__(self):
        return f"Clock[name={self.name}, id={self.id}]"


if __name__ == '__main__':
    # 定义闹钟对象
    clock1 = Clock()
    # 给闹钟属性赋值
    clock1.name = "早晨的闹钟"
    clock1.id = 1
    print(clock1)
    clock1.ring()
