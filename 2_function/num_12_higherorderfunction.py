"""
    sorted()函数:
        函数原理:
            把可迭代数据里面的元素, 一个一个的取出来, 放到key这个函数中去处理, 并按照函数中return的结果进行排序, 返回一个新的列表
        功能: 排序
        参数:
            iterable: 可迭代对象
            reverse: 可选参数, reverse=True ==> 降序, reverse=False ==> 升序, 默认为升序
            key: 可选参数, 函数对象, 可以是自定义函数, 也可以是内置函数
        返回值:排序后的可迭代对象
    map(func, *iterables)函数:
        功能: 对传入的可迭代数据中的每一个元素进行处理, 返回一个新的迭代器
        参数:
            func: 函数, 自定义函数或内置函数
            iterables: 可迭代数据
        返回值:
            返回一个新的迭代器
    reduce(func, *iterable)函数:
        注意: 使用前要先导入: from functools import reduce
        功能: 依次从可迭代数据中取出两个值, 放入到func函数中进行处理, 得到的处理结果和iterable中的第三个元素,
             再一起放到func函数中进行运算
        参数:
            func: 自定义或内置函数
            iterable: 可迭代数据
        返回值:最终的运算处理结果
    filter(func, iterable)函数:
        功能: 过滤器, 过滤数据-把iterable中的每个元素拿到func中进行处理, 如果函数返回True,则保留数据, 返回False,
             则丢弃数据
        参数:
            func: 自定义函数
            iterable: 可迭代数据
        返回值:保留数据组成的迭代器
"""
from functools import reduce

# 使用lambda表达式测试sorted()函数
print("sorted()函数执行结果: ")
my_list: list[dict] = [{"id": 1, "name": "郭鹏涛", "age": 25},
                       {"id": 2, "name": "陈欣妮", "age": 25},
                       {"id": 3, "name": "郭鹏强", "age": 22}]
list_sorted_test = sorted(my_list, key=lambda x: x["id"], reverse=True)  # reverse=True ==> 降序, reverse=False ==> 升序
print(list_sorted_test)
# 使用lambda表达式测试map()函数
print("map()函数执行结果: ")
list_map_test = map(lambda x: x ** 10, [1, 2, 3, 4])
print("迭代数据: ", list_map_test.__next__())
for map_data in list_map_test:
    print(map_data)
# 使用lambda表达式测试reduce()函数
print("reduce()函数执行结果: ")
list_reduce_test = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(list_reduce_test)
# 使用lambda表达式测试filter()函数
print("filter()函数执行结果:")
list_filter_test = filter(lambda x: True if x >= 3 else False, [3, 5, 2, 8, 0, -5])
print("迭代数据: ", list_filter_test.__next__())
for filter_data in list_filter_test:
    print(filter_data)
