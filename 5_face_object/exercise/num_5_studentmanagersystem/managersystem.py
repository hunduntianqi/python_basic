"""
    定义学生管理类, 用来管理学生信息
"""
from Student import Student


class ManagerSystem:
    # 定义类成员列表, 存储学生对象
    student_list: list[Student] = []

    # 定义类方法, 打印系统主页信息
    @classmethod
    def print_message(cls):
        print("============欢迎使用混沌管理系统============")
        print("1. 添加学生信息")
        print("2. 删除学生信息")
        print("3. 修改学生信息")
        print("4. 查询学生信息")
        print("5. 显示所有学生信息")
        print("6. 退出系统")

    # 定义方法, 添加学生信息
    def add_student(self):
        # 创建学生对象
        student = Student()
        while True:
            # 学生id
            student.set_id_num(int(input("请输入学生的学号:")))
            # 判断学生列表是否为空
            if len(ManagerSystem.student_list) == 0:
                # 系统中没有学生信息, 不会存在学号重复问题
                # 学生姓名
                student.set_name(input("请输入学生姓名:"))
                # 学生年龄
                student.set_age(int(input("请输入学生年龄:")))
                # 学生成绩
                student.set_score(float(input("请输入学生的成绩:")))
                ManagerSystem.student_list.append(student)
                print("学生{}的信息已添加成功".format(student))
                break
            else:
                # 系统中存在学生信息, 要检查学号是否重复
                # 遍历学生列表
                for student_judge in ManagerSystem.student_list:
                    if student.get_id_num() == student_judge.get_id_num():
                        print("学号重复, 请重新输入:")
                        break
                else:
                    # 不存在重复学号, 继续录入其他信息
                    # 学生姓名
                    student.set_name(input("请输入学生姓名:"))
                    # 学生年龄
                    student.set_age(int(input("请输入学生年龄:")))
                    # 学生成绩
                    student.set_score(float(input("请输入学生的成绩:")))
                    ManagerSystem.student_list.append(student)
                    print("学生{}的信息已添加成功".format(student))
                    break

    # 定义方法, 删除学生信息
    def del_student(self):
        # 判断系统中是否存在学生信息
        if len(ManagerSystem.student_list) == 0:
            print("系统中不存在学生信息, 无法删除学生信息!!!")
        else:
            id_num: int = int(input("请输入要删除学生的学号"))
            # 循环遍历查找要删除的学生
            for student in ManagerSystem.student_list:
                if student.get_id_num() == id_num:
                    ManagerSystem.student_list.remove(student)
                    print("学生{}的信息已从系统中删除!!".format(student.get_name()))
                    break
            else:
                print("你要删除的学生信息在系统中不存在, 请再检查一下!!")

    # 定义方法, 修改学生信息
    def change_student(self):
        # 判断系统中是否存在学生信息
        if len(ManagerSystem.student_list) == 0:
            print("系统中不存在学生信息, 无法修改学生信息!!!")
        else:
            id_num: int = int(input("请输入要修改学生的学号"))
            # 循环遍历查找对应学生
            for student in ManagerSystem.student_list:
                if student.get_id_num() == id_num:
                    # 是否修改学生学号
                    choose_id: str = input("请问是否修改学生学号(Yes/No):")
                    if choose_id == "Yes" or choose_id == "yes":
                        flag: bool = True
                        while flag:
                            id_num_change = int(input("请输入新学号:"))
                            # 判断学号是否与原学号一致
                            if id_num_change == id_num:
                                print("新学号不能与原学号重复, 请重新输入:")
                                continue
                            else:
                                # 循环判断系统中是否存在重复学号
                                for student_id_judge in ManagerSystem.student_list:
                                    if id_num_change == student_id_judge.get_id_num():
                                        print("该学号系统中已存在, 请重新输入: ")
                                else:
                                    # 不存在重复学号, 修改学号
                                    student.set_id_num(id_num_change)
                                    flag = False
                    choose_name: str = input("请问是否修改学生姓名(Yes/No):")
                    if choose_name == "Yes" or choose_name == "yes":
                        student.set_name(input("请输入学生修改后的姓名: "))
                    choose_age: str = input("请问是否修改学生年龄(Yes/No):")
                    if choose_age == "Yes" or choose_age == "yes":
                        student.set_age(int(input("请输入学生修改后的年龄: ")))
                    choose_score: str = input("请问是否修改学生成绩(Yes/No):")
                    if choose_score == "Yes" or choose_score == "yes":
                        student.set_score(float(input("请输入学生修改后的成绩: ")))
                    print("学生信息已修改成功!!")
                    break
            else:
                print("你要修改的学生信息在系统中不存在, 请再检查一下!!")

    # 定义方法, 查询学生信息
    def inquire_student(self):
        # 判断系统中是否存在学生信息
        if len(ManagerSystem.student_list) == 0:
            print("系统中不存在学生信息, 请先添加学生信息!!!")
        else:
            id_num: int = int(input("请输入要查询学生的学号"))
            # 循环遍历查找对应的学生
            for student in ManagerSystem.student_list:
                if student.get_id_num() == id_num:
                    print("学号\t学生姓名\t学生年龄\t学生成绩")
                    print("{}\t{}\t{}\t\t{}".format(student.get_id_num(), student.get_name(), student.get_age(),
                                                    student.get_score()))
                    break
            else:
                print("你要查找的学生信息在系统中不存在, 请再检查一下!!")

    # 定义方法, 显示所有学生信息
    def print_all_student(self):
        # 判断学生列表是否为空
        if len(ManagerSystem.student_list) == 0:
            print("系统中无学生信息, 无法查看学生信息")
        else:
            print("学号\t学生姓名\t学生年龄\t学生成绩")
            # 循环遍历列表
            for student in ManagerSystem.student_list:
                # 打印学生信息
                print("{}\t{}\t{}\t\t{}".format(student.get_id_num(), student.get_name(), student.get_age(),
                                                student.get_score()))
