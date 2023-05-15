from Cat import Cat
from Dog import Dog

if __name__ == '__main__':
    # 创建狗类对象
    dog = Dog("旺财")  # type: Dog
    # 创建Cat类对象
    cat = Cat("汤姆")  # type: Cat
    # 访问共有方法
    dog.eat()  # 多态存在, 实际调用子类重写的方法
    dog.drinking()
    # 访问Dog类独有方法
    dog.look_door()
    print("===============")
    # 访问共有方法
    cat.eat()  # 多态存在, 实际调用子类重写的方法
    cat.drinking()
    # 访问Cat类独有方法
    cat.grab_mouse()
