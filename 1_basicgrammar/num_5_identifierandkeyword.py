"""
    标识符:
        指python中定义的变量名, 函数名, 类名等, 标识符要见名知意
        命名规则:
            a. 标识符由字母, 数字和下划线组成
            b. 不能以数字开头
            c. 不能与关键字重名
        注意: Python中标识符区分大小写
        命名法则:
            1. 小驼峰命名法(Python一般不用):
                第一个单词以小写字母开始, 第二个单词的首字母大写, 例如: myName, aDog
            2. 大驼峰命名法(一般为定义类名使用):
                每一个单词的首字母都采用大写字母, 例如: FirstName, LastName
            3. 使用下划线来链接所有的单词(Python中使用的命名规则), 例如: send_buf
    关键字:
        指python中已经使用的具有特殊功能和含义的标识符
        查看python中的关键字:
            import keyword
            print(keyword.kwlist)
"""

import keyword

list_keyword = keyword.kwlist

for kw in list_keyword:
    print(kw)
