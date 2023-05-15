import Student

if __name__ == '__main__':
    # 创建学生类对象
    student1 = Student.Student("郭鹏涛", 25, "男")  # type:Student
    student2 = Student.Student("郭鹏强", 22, "男")  # type:Student
    student3 = Student.Student("陈欣妮", 25, "女")  # type:Student
    print(student1)
    print(student2)
    print(student3)
    # 直接访问对象私有属性
    # print(student1.__name)  报错 ==> AttributeError: 'Student' object has no attribute '__name'
    # print(student1.name)  报错 ==> AttributeError: 'Student' object has no attribute 'name'
    # 访问对象的私有属性
    print("name: {}".format(student1._Student__name))
    print("age: {}".format(student1._Student__age))
    print("sex: {}".format(student1._Student__sex))
    # 调用对象私有方法
    student1._Student__secret()
    # 调用对象公共方法
    student1.study()
    # 根据模仿Java get&set方法, 修改类的私有属性
    student1.set_name("混沌天帝")
    student1.set_age(24)
    student1.set_sex("未知")
    print(student1)
