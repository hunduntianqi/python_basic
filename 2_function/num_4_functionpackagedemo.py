""" 函数封装练习 """


# 打印九九乘法表
def jiujiu(n=0):
    '''
    函数功能:打印九九乘法表
    n:默认等于0, 九九乘法表正向输出, 否则反向输出
    :return:
    '''
    rs = 0
    if n == 0:
        rs = range(1, 10)
    else:
        rs = range(9, 0, -1)
    for i in rs:
        for j in range(1, i + 1):
            print("{} * {} = {}\t".format(j, i, i * j), end='')
        print()


# 打印矩形
def juxing(n=0):
    if n == 0:
        for x in range(1, 201):
            print('#', end='')
            if x % 20 == 0:
                print()
    else:
        for x in range(1, 11):
            if x > 1 and x < 10:
                for y in range(1, 21):
                    if y == 1 or y == 20:
                        print('#', end='')
                    else:
                        print(' ', end='')
            else:
                for y in range(1, 21):
                    print('#', end='')
            print()


if __name__ == '__main__':
    # 调用函数打印乘法口诀表
    jiujiu(1)
    jiujiu()
    jiujiu(1)
    jiujiu()
    jiujiu(1)
    jiujiu()
    jiujiu(1)
    jiujiu()
    # 调用函数打印矩形
    juxing()
