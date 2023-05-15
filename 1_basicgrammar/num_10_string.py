"""
    字符串:
        python中的一种基本数据类型, 使用非常广泛, 在python中, 凡是''和""包裹的内容都是字符串
        常用方法:
            1.len(字符串)：统计字符串长度
            2.大字符串.count(小字符串)：统计小字符串在大字符串中出现的次数
            3.大字符串.index(小字符串)：获取第一个小字符串出现的索引位置(子字符串不存在,程序会报错)
        判断相关方法:
            1. String.isspace(): 如果String中只包含空格/'\n'/'\t'/'\r',则返回True
            2. String.isalnum(): 如果String中至少有一个字符, 并且所有字符都是字母或数字，则返回True
            3. String.isalpha(): 如果String中至少有一个字符, 并且所有字符都是字母则返回True
            4. String.isdecima(): String中只包含数字则返回True, 全角数字
            5. String.isdigit(): 如果string只包含数字则返回True, 全角数字、(1)、\u00b2
            6. String.isnumeric(): 如果string只包含数字则返回True, 全角数字、汉字数字
            7. String.istitle(): 如果String中每个单词首字母大写, 则返回True
            8. String.isupper(): 如果String中全部为大写字符, 则返回True
            9. String.islower(): 如果String中全部为小写字符, 则返回True
        查找和替换相关方法:
            1. String.startswith(str):检查字符串是否以 str 开头, 是则返回True
            2. String.endswith(str): 检查字符串是否以 str 结束, 是则返回True
            3. String.find(str, start=0, end=len(string)): 检查str是否包含在String中, 如果start和end指定范围,
                则在指定范围内进行查找, 查找到返回开始索引, 否则返回 -1
            4. String.rfind(str,stat=0,end=len(string)): 类似于find函数, 从右侧开始查找
            5. String.index(str,stat=0,end=len(string)): 和find()方法类似, 若str不在string会报错
            6. String.rindex(str,stat=0,end=len(string)): 类似于index(), 从右边开始
            7. String.replace(old_str,new_str,num=string.count(old)):把string中的old_str替换成new_str,若指定num,
                则替换次数不超过指定次数
        大小写转换方法:
            1. String.capitalize(): 将字符串第一个字符转换为大写
            2. String.title(): 将字符串中每个单词首字母转换为大写
            3. String.lower(): 将字符串中所有字符转换为小写
            4. String.upper(): 将字符串中的所有字符转换为大写
            5. String.swapcase(): 将字符串中的大小写字符翻转
        文本对齐方法:
            1. String.ljust(width): 返回一个原字符串左对齐, 并使用空格填充至长度width的新字符串
            2. String.rjust(width): 返回一个原字符串右对齐, 并使用空格填充至长度width的新字符串
            3. String.center(width): 返回一个原字符串居中,并使用空格填充至长度width的新字符串
        去除空白字符方法:
            1. String.lstrip(): 去除String左边的空白字符
            2. String.rstrip(): 去除String右边的空白字符
            3. String.strip(): 去除String左右两侧的空白字符
        拆分和连接字符串方法:
            1. String.partition(str): 把字符串string分成一个3元素的元组(str前面,str,str后面)
            2. String.rpartition(str): 右partition类似,从右边开始查找
            3. String.split(str="", num): 以str为分隔符切片string,如果num有指定值,则仅分隔num+1个子字符串,
                str默认包含'\t', '\r', '\n'和空格
            4. String.splitlines(): 按照行('\r','\n','\t')分隔, 返回一个包含各行元素的列表
            5. String.join(list[str]): 以string为分隔符, 将list中所有的元素(字符串)合并为一个新的字符串
    字符串切片:
        作用: 通过指定索引, 可以获取字符串中的某一段字符
        格式: string[起始索引: 结束索引: 步长]
        注意:
            切片时, 起始索引和结束索引都可以使用负数, 负数表示从右向左, 第一个索引是-1
        切片实现字符串逆序通用公式 ==> string[::-1]
"""
if __name__ == '__main__':
    # 1.判断空白字符
    space_str = '  \t\r\n'
    print(space_str.isspace())

    # 2.判断字符串中是否只包含数字
    num_str = '123456'
    print(num_str.isdecimal())
    num_str = '\u00b2'
    print(num_str.isdigit())
    num_str = '一'
    print(num_str.isnumeric())

    # 1.判断是否以指定字符串开始
    hello_str = 'hello world'
    print(hello_str.startswith('H'))

    # 2.判断是否以指定字符串结束
    print(hello_str.endswith('lD'))

    # 3.查找指定字符串
    # index方法同样可以查找指定字符串在大字符串中的索引
    # 区别在于, 若查找字符串不存在, index方法会报错, 而find方法则会返回-1, 不会报错
    print(hello_str.find('ll'))

    # 4.替换字符串
    # replace方法执行完成会返回一个新的字符串,不会改变原来的字符串！！！
    print(hello_str.replace('l','m',1))

    poem = ['  登鹳雀楼  ',
            ' 王之涣  ',
            '  白日依山尽     ',
            ' 黄河入海流 ',
            '欲穷 千里目',
            '更 上一层 楼']

    for poem_str in poem:
        print('↑{}↑'.format(poem_str.strip().center(5,'　')))