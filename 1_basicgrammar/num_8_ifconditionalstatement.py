"""
    if条件语句:
        格式一 if 语句:
            if 条件语句:
                条件成立执行代码
        格式二 if...else 语句:
            if 条件语句:
                条件成立执行代码
            else:
                条件不成立执行代码
        格式三 if...elif...else 语句:
            if 条件语句1:
                条件语句1成立执行代码
            elif 条件语句2:
                条件语句2成立执行代码
                ...
            else:
                所有条件不成立执行的代码
    if条件语句实现三目运算符:
        条件成立返回值 if 条件表达式 else 条件不成立返回值
"""
import random


# 年龄判断
def judge_age(age: int):
    if age >= 18:
        print('你已经成年了,可以喝酒，可以进网吧嗨皮！！！')
    elif 12 < age < 18:
        print('你还未成年,不能喝酒,不能去网吧')
    elif 0 < age <= 12:
        print('你是一个儿童！！！')
    else:
        print('你不是人')


# 猜拳游戏
def finger_guessing_game(player_finger: int):
    """
        猜拳游戏:
            0 ==> 石头
            1 ==> 剪刀
            2 ==> 布
    """
    # 使用随机数对象模拟电脑出拳
    computer_finger: int = random.randint(0, 2)
    print('玩家: {}'.format(player_finger))
    print('电脑: {}'.format(computer_finger))
    if player_finger == computer_finger:
        print('玩家与电脑出拳一样, 本轮平局!!')
    elif (player_finger == 0 and computer_finger == 1) or (player_finger == 1 and computer_finger == 2) or (
            player_finger == 2 and computer_finger == 0):
        print('玩家战胜了电脑, 可喜可贺!!!')
    elif (player_finger == 1 and computer_finger == 0) or (player_finger == 2 and computer_finger == 1) or (
            player_finger == 0 and computer_finger == 2):
        print('电脑取得了本轮猜拳游戏的胜利!!')


if __name__ == '__main__':
    # age = int(input('请输入你的年龄：\n'))
    # judge_age(age)
    finger_guessing_game(0)
    # if条件语句三目运算符实现
    print("偶数" if 2 % 2 == 0 else "奇数")  # 偶数
