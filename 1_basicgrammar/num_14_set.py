"""
    集合 ==> set:
        主要特点: 元素无序且不重复, 不支持下标索引, 由一系列键组成的可变散列容器
        散列: 对键进行哈希运算, 确定在内存中的存储位置, 数据存储无先后顺序
        集合定义:
            set_name = {元素1, 元素2, ....}
        空集合定义: set_name = set()
        集合常用方法:
            1. set.add(data): 将指定数据添加到集合中
            2. set.remove(data): 将指定数据从集合中删除
            3. set.pop(): 从集合中随机删除元素并将删除后的数据返回
            4. set.clear(): 清空集合元素
            5. set.difference(set2): 获取set中有, set2没有的元素, 并存入一个新的集合返回
            6. set.difference_update(set2): 在set内, 删除和set2相同的元素
            7. set.union(set2): 将set与set2中的元素合并后返回新的集合(重复元素会去重)
            8. len(set): 获取集合中元素的个数
        集合遍历:
            for data in set:
                print(data)
            注意: 集合无索引, 不可以使用while循环遍历
        集合转换为列表 ==> list(set_name)
        集合转换为元组 ==> tuple(set_name)
        集合推导式:
            根据可迭代对象, 简单的构建集合
            语法: set_name = [表达式 for 变量名 in 可迭代对象 if 筛选条件(可省略)]
            注意: 使用集合推导式创建集合时, 必须指定集合类型注解
"""

if __name__ == '__main__':
    # 定义集合
    my_set: set = {"黑马程序员", '传智教育', 'python', 'C++', 'java', '传智教育', 'python', 'C++', 'java'}
    # 定义空集合
    set_empty = set()
    print(set_empty)
    print('mySet = {}'.format(my_set))  # mySet = {'python', 'java', '黑马程序员', 'C++', '传智教育'}
    # 集合添加元素
    my_set.add("123")
    print(my_set)
    # 删除集合元素
    my_set.remove("C++")
    print(my_set)
    # 随机删除集合元素
    data = my_set.pop()
    print("被删除的元素是'{}', my_set = {}".format(data, my_set))
    # # 清空集合元素
    # my_set.clear()
    # print(my_set)
    # 定义一个新的集合
    set2 = {"123", "python"}
    set3 = my_set.difference(set2)
    print(my_set)
    print(set2)
    print(set3)
    # 遍历集合
    for data in my_set:
        print(data)
    print(list(my_set))
    print(tuple(my_set))
    # 集合推导式创建集合
    my_set2 = {value for value in [1, 1, 2, 4] if value % 2 != 0}  # type: set[int]
    print(my_set2)
