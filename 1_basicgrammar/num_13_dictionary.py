"""
    字典 ==> dict:
        是除列表外Python中最灵活的数据类型, 是一系列键值对组成的可变散列容器
        散列: 对键进行哈希运算, 确定在内存中的存储位置, 数据存储无先后顺序
        1）字典通常用来存储用于描述物体相关信息的数据
        2）字典和列表的区别：
            1.列表是有序的对象集合
            2.字典是无序的对象集合
        3）字典用 {} 定义:
            dict_name = {}
        4）字典使用键值对存储数据，键值对之间使用 , 分隔
            1.键 key 是索引
            2.值 value 是数据
            3.键和值之间使用 : 分隔
            4.键必须是惟一的
            5.value 可以取任何数据类型,但 key 只能用字符串, 数字或元组(不可变数据类型)
        字典常用方法:
            1. 字典.keys(): 获取所有key列表
            2. 字典.values(): 获取所有value列表
            3. 字典.items(): 获取所有(key,value)元组列表
            4. len(dict_name): 获取字典中键值对的数量
            5. 字典[键]: 取出对应键的值, 键名不存在程序会报错;
                dict.get(key_name): 获取对应键的值, 键名不存在会返回None
            6. 新增键值对: 字典[新增的键] = 数据
            7. 修改键值对: 字典[已经有的键] = 修改后的数据
            8. 删除键值对: 字典.pop(要删除的键)
            9. 合并字典: 字典1.update(字典2), 合并后结果: 将字典2的键值对复制到字典1中, 若有重复的键, 会覆盖字典1中原来的值
            10. 字典.clear(): 清空字典
        字典推导式:
            使用简易方法, 根据可迭代对象创建字典
            dict_name: dict[key_type, value_type] = {key:value for key in 可迭代对象 if 判断条件(可省略)}
"""

if __name__ == '__main__':
    # 根据字典推导式创建字典
    dict_name: dict[int, int] = {key: key ** 2 for key in range(10) if key % 2 == 0}
    print(dict_name)
    # 同时从多个列表取出元素构建字典
    list_key = [101, 102, 103]  # type: list[int]
    list_value = ['张无忌', '赵敏', '周芷若']  # type: list[str]
    dict_name2: dict[int, str] = {list_key[num]: list_value[num] for num in range(len(list_key))}
    print(dict_name2)
    # 使用items()方法遍历字典
    for key, value in dict_name.items():
        print("{} ==> {}".format(key, value))
