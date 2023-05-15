"""
    名片管理系统功能模块
"""


# 定义名片类
class Card:
    # 定义类属性列表, 存储对象
    card_list = []  # type: list[Card]

    def __init__(self, name: str, phone: str, qq: str, email: str):
        self.__name = name
        self.__phone = phone
        self.__qq = qq
        self.__email = email

    # 重写__str__方法, 打印对象信息
    def __str__(self):
        return 'Card[name:{}, phone:{}, qq:{}, email:{}]'.format(self.__name, self.__phone, self.__qq, self.__email)

    # 定义类方法, 展示当前类创建对象个数
    @classmethod
    def object_num(cls):
        print('当前系统名片数量为:{}'.format(len(Card.card_list)))


# 定义全局列表, 存储Card对象
# card_list: list[Card] = []


# 定义函数显示主界面
def show():
    print()
    print("==============欢迎使用混沌名片管理系统==============")
    print('1. 新增名片')
    print('2. 显示所有名片')
    print('3. 查询指定名片信息')
    print('4. 修改名片信息')
    print('5. 删除指定名片')
    print('6. 显示当前系统名片数量')
    print('7. 退出系统')
    print("==================================================")
    print()


# 定义函数新增名片
def add_card():
    # 创建名片对象
    card = Card.__new__(Card)
    name = input('请输入名片姓名:\n')
    card._Card__name = name
    phone = input('请输入手机号:\n')
    card._Card__phone = phone
    qq = input('请输入QQ号:\n')
    card._Card__qq = qq
    email = input('请输入邮箱地址:\n')
    card._Card__email = email
    # 名片对象添加到列表中
    Card.card_list.append(card)
    print('名片{}添加成功！！'.format(card._Card__name))


# 定义函数显示所有名片
def show_all_card():
    if len(Card.card_list) == 0:
        print('当前系统无名片信息, 请先添加名片！！')
        return
    for card in Card.card_list:
        print(card)


# 定义函数查询指定名片
def query_card():
    if len(Card.card_list) == 0:
        print('当前系统无名片信息, 请先添加名片！！')
        return
    name = input('请输入查询名片姓名:\n')
    # 遍历列表寻找对应名片
    for card in Card.card_list:
        if card._Card__name == name:
            print(card)
            return
    print('当前系统无 {} 名片信息, 请检查输入是否正确！！'.format(name))


# 定义函数修改名片信息
def change_card_message():
    if len(Card.card_list) == 0:
        print('当前系统无名片信息, 请先添加名片！！')
        return
    name = input('请输入要修改名片的姓名:\n')
    # 遍历列表, 寻找对应名片
    for card in Card.card_list:
        if card._Card__name == name:
            name = input('请输入修改后的姓名(无需修改请输入n/N):\n')
            if name == 'n' or name == 'N':
                pass
            else:
                card._Card__name = name
            phone = input('请输入修改后的手机号(无需修改请输入n/N):\n')
            if phone == 'n' or phone == 'N':
                pass
            else:
                card._Card__phone = phone
            qq = input('请输入修改后的QQ号(无需修改请输入n/N):\n')
            if qq == 'n' or qq == 'N':
                pass
            else:
                card._Card__qq = qq
            email = input('请输入修改后的邮箱(无需修改请输入n/N):\n')
            if email == 'n' or email == 'N':
                pass
            else:
                card._Card__email = email
            print('信息修改成功')
            return
    print('系统无对应名片信息, 请检查输入是否有误！！')


# 定义函数删除指定名片
def delete_card():
    if len(Card.card_list) == 0:
        print('当前系统无名片信息, 请先添加名片！！')
        return
    name = input('请输入要删除名片的姓名:\n')
    # 遍历列表, 寻找要删除的名片
    for card in Card.card_list:
        if card._Card__name == name:
            card_index = Card.card_list.index(card)
            del Card.card_list[card_index]
            print('名片 {} 已删除！！'.format(card._Card__name))
            return
    print('系统无对应名片信息, 请检查输入是否有误！！')
