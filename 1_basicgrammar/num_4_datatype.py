"""
    Python中存在六种标准数据类型:
        1. 数字型 ==> Number:
            包括 int, float, bool, complex
        2. 字符串 ==> String
        3. 列表 ==> List
        4. 元组 ==> Tuple
        5. 字典 ==> Dictionary
        6. 集合 ==> Set
    可变数据类型:
        类似于引用传递, 在不改变地址值时数据可变
        1. 列表 ==> List
        2. 字典 ==> Dictionary
        3. 集合 ==> Set
    不可变数据类型:
        类似于值传递, 在不改变地址值时, 数据不可变, 每次修改赋值实际是改变了地址值, 相当于创建了同名变量, 重新分配了内存
        1. 数字型 ==> Number
        2. 字符串 ==> String
        3. 元组 ==> Tuple
    数据类型转换:
        1. 隐式类型转换 ==> 自动完成, 不需要人为干预
            在运算时, 范围小的数据类型会自动转换为范围大的数据类型参与计算
            bool -> int -> float -> complex
        2. 强制类型转换:
            int(variable_name): 将变量强制转换为 int 类型
            float(variable_name): 将变量强制转换为 float 类型
            complex(real[,imag]): 创建一个复数, real为实部, imag为虚部
            str(variable_name): 将变量强制转换为字符串类型
            repr(x): 将对象x转换为表达式字符串
            eval(str): 用来计算在字符串中的有效Python表达式, 并返回一个对象
            tuple(s): 将序列 s 转换为一个元组
            list(s): 将序列 s 转换为一个列表
            set(s): 将序列 s 转换为一个可变集合
            dict(d): 创建一个字典, 序列d 必须是一个(key, value)元组序列
            frozenset(s): 将序列 s 转换为一个不可变集合
            chr(x): 将整数 x 转换为一个字符
            ord(x): 将一个字符转换为它的整数值
            hex(x): 将一个整数转换为一个十六进制字符串
            oct(x): 将一个整数转换为一个八进制字符串
            bin(x): 将一个整数转换为一个二进制字符串
"""