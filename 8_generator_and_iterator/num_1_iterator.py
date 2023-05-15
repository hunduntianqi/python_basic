"""
    迭代器(Iterator):
        使python中最具特色的功能之一, 是访问集合元素的一种方式
        集合元素:字符串, 列表, 元组, 字典, 集合set
        是一个可以记住访问遍历位置的对象, 从集合中的第一个元素开始访问, 直到集合中所有元素被访问完毕
        迭代器只能从前往后依次遍历, 不能后退
        迭代器是一个能被next()函数调用并不断返回下一个值的对象
        iter():
            功能: 把一个可迭代的对象, 转化为一个迭代器对象
            参数: 可迭代对象(str, list, tuple, dict, set, range)
            返回值: 迭代器对象
            注意:迭代器一定是可迭代对象, 可迭代对象不一定是迭代器
            迭代器取值:
                1. next(): 调用一次取一次, 直到数据被取完为止
                2. list(): 使用list函数直接取出迭代器中的所有数据
                3. for循环遍历迭代器数据
            迭代器取值的特点:
                取出一个少一个, 直到全部取完为止, 再次取值会报错
"""

# 定义一个列表, 是一个可迭代对象
f4 = ['赵四', '刘能', '小沈阳', '海参炒面']
# for 循环遍历
for i in f4:
    print(i)
# 将可迭代对象转换为迭代器
res = iter(f4)
print(type(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# print(next(res)) 超出可迭代范围, 报错
