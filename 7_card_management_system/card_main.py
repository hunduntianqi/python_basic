import card_util


# 定义方法, 执行名片管理系统功能
def main():
    # while使用死循环保证程序一直运行
    while True:
        # 显示主界面
        card_util.show()
        choose = input('请按照提示操作:\n')
        if choose == '1':
            card_util.add_card()
        elif choose == '2':
            card_util.show_all_card()
        elif choose == '3':
            card_util.query_card()
        elif choose == '4':
            card_util.change_card_message()
        elif choose == '5':
            card_util.delete_card()
        elif choose == '6':
            card_util.Card.object_num()
        elif choose == '7':
            print('正在退出系统, 感谢您的使用, 下次再见~~~')
            return
        else:
            print('您输入的操作有误, 请按照提示操作！！')


if __name__ == '__main__':
    main()
