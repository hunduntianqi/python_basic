"""
    函数版学生管理系统
        实现功能:
            1. 打印主页面, 展示系统功能
            2. 添加学生
            3. 删除学生
            4. 修改学生信息
            5. 查询学生信息
            6. 显示所有学生信息
            7. 退出系统
"""


# 定义函数, 打印系统主页面
def print_menu():
    print("============欢迎使用混沌管理系统============")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("6. 退出系统")


# 定义函数, 添加学生信息
def add_student(list_student: list[dict]):
    # 定义字典, 存储学生信息
    dict_student = {}  # type:dict
    while True:
        # 添加学生ID信息
        dict_student["id"] = int(input("请输入添加学生的ID号:"))
        # 判断id号是否重复
        if len(list_student) == 0:
            # 添加学生姓名
            dict_student["name"] = input("请输入添加学生的姓名:")
            # 添加学生的性别
            dict_student["sex"] = input("请输入添加学生的性别信息:")
            # 添加学生手机号
            dict_student["phone"] = input("请输入添加学生的联系方式:")
            # 将包含学生信息的字典存入列表
            list_student.append(dict_student)
            print("id为:{}; 姓名为: '{}'的学生信息已添加成功!!".format(dict_student["id"], dict_student["name"]))
            break
        else:
            # 循环遍历比较是否有重复id
            for student in list_student:
                if student["id"] == dict_student["id"]:
                    print("该学生id已存在, 请重新输入!!")
                    break
            else:
                # 添加学生姓名
                dict_student["name"] = input("请输入添加学生的姓名:")
                # 添加学生的性别
                dict_student["sex"] = input("请输入添加学生的性别信息:")
                # 添加学生手机号
                dict_student["phone"] = input("请输入添加学生的联系方式:")
                # 将包含学生信息的字典存入列表
                list_student.append(dict_student)
                print("id为:{}; 姓名为: '{}'的学生信息已添加成功!!".format(dict_student["id"], dict_student["name"]))
                break


# 定义函数, 删除学生信息
def del_student(list_student: list[dict]):
    # 判断列表是否为空
    if len(list_student) == 0:
        print("系统中无学生信息, 无法删除学生信息")
    else:
        id_student: int = int(input("请输入要删除学生的id号:"))
        # 遍历列表, 找到对应学生后从列表中删除学生信息
        for student in list_student:
            if student["id"] == id_student:
                # 找到对应学生信息, 从列表中删除
                list_student.remove(student)
                print("id为{}的学生信息已删除!!".format(student["id"]))
                break
        else:
            print("你要删除的学生信息在系统中不存在, 请再检查一下, 谢谢")


# 定义函数, 修改学生信息
def change_student(list_student: list[dict]):
    # 判断列表是否为空
    if len(list_student) == 0:
        print("系统中无学生信息, 无法修改学生信息")
    else:
        id_student: int = int(input("请输入要修改学生信息的id号:"))
        # 遍历列表, 找到对应学生后修改学生信息
        for student in list_student:
            if student["id"] == id_student:
                # 找到对应学生信息, 修改指定信息
                for key in student.keys():
                    flag_judge = input("请问是否要修改学生的{}(Yes/No): ".format(key))
                    if flag_judge == "Yes" or flag_judge == "yes":
                        if key == "id":
                            flag: bool = True  # 定义变量控制循环是否继续
                            while flag:  # 循环判断保证id不能与列表中已有数据重复
                                change_id = int(input("请输入修改后的id:"))
                                if change_id == id_student:
                                    print("修改后的id不能与原id一致, 请重新输入: ")
                                else:
                                    for student_id_judge in list_student:
                                        if change_id == student_id_judge["id"]:
                                            print("id重复, 请重新输入: ")
                                            break
                                    else:
                                        # 不存在重复id, 修改对应学生id
                                        student[key] = change_id
                                        # 修改flag值, 结束死循环
                                        flag = False
                        else:
                            student[key] = input("请输入修改后的信息:")
                print("id为{}的学生信息已修改!!".format(id_student))
                break
        else:
            print("你要修改的学生信息在系统中不存在, 请再检查一下, 谢谢")


# 定义函数, 查询指定学生信息
def inquire_student(list_student: list[dict]):
    # 判断列表是否为空
    if len(list_student) == 0:
        print("系统中无学生信息, 无法查看学生信息")
    else:
        id_student: int = int(input("请输入要查询学生信息的id号:"))
        # 遍历列表, 找到对应学生后展示学生信息
        for student in list_student:
            if student["id"] == id_student:
                print("id为{}的学生信息为:".format(id_student))
                print("id\tname\tsex\t\tphone")
                print("{}\t{}\t{}\t{}".format(student["id"], student["name"], student["sex"], student["phone"]))
                break
        else:
            print("你要查询的学生信息在系统中不存在, 请再检查一下, 谢谢")


# 定义函数, 显示所有学生信息
def print_all_message(list_student: list[dict]):
    # 判断列表是否为空
    if len(list_student) == 0:
        print("系统中无学生信息, 无法查看学生信息")
    else:
        print("id\tname\tsex\t\tphone")
        # 循环遍历列表
        for student in list_student:
            # 打印学生信息
            print("{}\t{}\t{}\t{}".format(student["id"], student["name"], student["sex"], student["phone"]))


# 定义主函数, 实现系统功能
def main_func():
    # 定义列表, 存储学生信息
    list_student = []  # type:list[dict]
    # 进入系统, 展示主页面信息
    print_menu()
    while True:
        # 定义变量, 接受用户输入信息
        user_choose = input("请选择您要办理的业务:")
        if user_choose == "1":
            # 添加学生信息
            print("======添加学生信息======")
            add_student(list_student)
        elif user_choose == "2":
            # 删除指定学生信息
            print("======删除学生信息======")
            del_student(list_student)
        elif user_choose == "3":
            # 修改指定学生信息
            print("======修改学生信息======")
            change_student(list_student)
        elif user_choose == "4":
            # 查询指定学生信息
            print("======查询学生信息======")
            inquire_student(list_student)
        elif user_choose == "5":
            # 显示所有学生信息
            print("======显示所有学生信息======")
            print_all_message(list_student)
        elif user_choose == "6":
            # 退出系统
            print("======退出系统======")
            return
        print_menu()


if __name__ == '__main__':
    main_func()
