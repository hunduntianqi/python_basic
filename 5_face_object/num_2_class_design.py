"""
    类的设计:
        类名: 这类事物的名字, 见名知意, 满足大驼峰命名法
            大驼峰命名法:
                1. 每个单词首字母大写
                2. 单词与单词之间没有下划线
        属性: 这类事物具有什么样的特征, 例如: 姓名, 年龄, 身高等
        方法: 这类事物具有什么样的行为, 例如: 跑, 跳, 飞行等
        类的定义:
            class class_name(object):
                property_name = start_value
                def method_name1(self,参数列表):
                    pass
                def method_name2(self,参数列表):
                    pass
            1. 方法的定义与函数几乎一样, 方法的第一个参数必须是self
            2. 定义属性时, 初始化值如果不确定, 可以将其设置为None
            3. self参数：
                由那一个对象调用类的方法,方法内的self就是哪一个对象的引用
                1. 在类的方法内部, self就表示当前调用方法的对象自己
                2. 调用方法时, 不需要传递self参数
                3. 在方法内部：
                    a. 可以通过self.访问对象的属性
                    b. 可以通过self.调用其他的对象方法
            4. object是Python的最顶级父类
            5. 定义类名一般要满足大驼峰命名法
        创建类的对象:
            object_name = class_name()
            通过对象访问属性和方法:
                a. 访问属性: object_name.property_name
                b. 访问方法: object_name.method_name()
        dir(object_name)函数: 可以查看对象内的所有属性及方法
        python的内置属性 / 方法:
            '__method_name__' / '__property_name__' 格式的属性或方法是内置属性或方法
            __new__(): 在创建类的对象时被自动调用, super().__new__(cls) ==> 为对象分配内存
            __init__(): 对象初始化时, 自动调用, 专门用来定义一个类具有哪些属性的方法, 类似于java构造器
                __init__()带参创建对象: object_name = class_name(属性初始化值)
                __init__()带参创建无初始化值对象: object_name = class_name.__new__(class_name)
                __init__()不带参创建对象: object_name = class_name()
                注意: 将每个实例属性初始值设置为None, 在创建对象时也可以不传递参数, 不会报错, 由此模拟Java无参构造和带参构造同时存在
            __del__(): 对象从内存中销毁时, 自动调用, 该方法执行意味着对象被销毁, 生命周期结束
            __str__(): 返回对象的描述信息, 在使用print(object_name) / str(object_name) 时调用,
                       要求必须返回一个字符串, 类似于java的toString()方法
"""
