from Cat import Cat
from Dog import Dog

if __name__ == '__main__':
    # 创建狗类对象
    dog = Dog("旺财")
    # 创建Cat类对象
    cat = Cat("汤姆")
    # 访问共有方法
    dog.eat()
    dog.drinking()
    # 访问Dog类独有方法
    dog.look_door()
    print("===============")
    # 访问共有方法
    cat.eat()
    cat.drinking()
    # 访问Cat类独有方法
    cat.grab_mouse()
