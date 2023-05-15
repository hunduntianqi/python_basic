"""
    学生管理系统实现功能:
        1. 打印主页面, 展示系统功能
        2. 添加学生
        3. 删除学生
        4. 修改学生信息
        5. 查询学生信息
        6. 显示所有学生信息
        7. 退出系统
"""

from ManagerSystem import ManagerSystem

if __name__ == '__main__':
    # 1. 创建学生管理系统对象
    manager_student_system = ManagerSystem()
    # 2. 初始登录, 展示主页面
    ManagerSystem.print_message()
    while True:
        choose_user = input("请输入你要办理的业务序号:")
        if choose_user == "1":
            # 添加学生信息
            manager_student_system.add_student()
        if choose_user == "2":
            # 删除学生信息
            manager_student_system.del_student()
        if choose_user == "3":
            # 修改学生信息
            manager_student_system.change_student()
        if choose_user == "4":
            # 查询指定学生信息
            manager_student_system.inquire_student()
        if choose_user == "5":
            # 展示所有学生信息
            manager_student_system.print_all_student()
        if choose_user == "6":
            # 退出系统
            print("退出系统...")
            break
        ManagerSystem.print_message()
