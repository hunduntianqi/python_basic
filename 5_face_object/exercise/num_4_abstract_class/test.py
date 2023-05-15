from Student import Student
from Teacher import Teacher
from Person import Person

if __name__ == '__main__':
    # 创建学生对象
    student = Student("郭鹏涛", 25)  # type: Person
    print(type(student))
    # 创建老师对象
    teacher = Teacher("陈欣妮", 25)  # type:Person
    print(type(teacher))
    # 调用重写后的方法
    student.work()
    teacher.work()
    # 创建Person对象(抽象类不能被实例化创建对象)
    # person = Person("隔壁老王", 35)  报错 ==> TypeError: Can't instantiate abstract class Person with abstract method work
