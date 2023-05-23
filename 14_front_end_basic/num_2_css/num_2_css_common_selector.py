"""
    1. 常用兼容性选择器:
        1.1 html选择器(标签选择器):
            指把html标签作为选择器使用
            html标签 {属性:值;属性:值;...}
            例:p{color:blue;font-family:隶书;font-size:50px} /*网页中所有的p标签都使用此样式*/
        1.2 class类选择器:
            指.class名来定义的选择器
            格式1: .类名{属性:值;属性:值;...} /*class属性值为此类名的所有标签使用此样式*/
            格式2: 标签名.类名{属性:值;属性:值;...} /*class属性值为此类名的对应标签使用此样式*/
        1.3 Id选择器:
            #id{属性:值;属性:值;...} /*id属性值为此id的使用此样式*/
        1.4 关联选择器(包含选择器):
            格式: 标签1 标签2 ...{属性:值;属性:值;...} /*满足对应标签嵌套规则的使用此样式*/
        1.5 组合选择器(选择符组):
            选择器1, 选择器2, 选择器3, ...{属性:值;属性:值;...} /*由逗号隔开的所有选择器使用此样式*/
        1.6 伪类(伪元素)选择器:
            格式: 标签名:伪类名{属性:值;属性:值;...}
            例: a:link{color:#FF0000; text-decoration:none}
    2. 其他选择器:
        2.1 关系选择器:
            标签1 标签2 {属性:值;属性:值;...}: 标签1下面的所有标签2使用此样式
            标签1>标签2 {属性:值;属性:值;...}: 标签1下面直接的标签2使用此样式
            标签1+标签2 {属性:值;属性:值;...}: 与标签1平级的在标签1之后紧邻的标签2使用此样式
            标签1~标签2 {属性:值;属性:值;...}: 与标签1平级的所有标签2使用此样式
        2.2 属性选择器:
            标签名[属性] {属性:值;属性:值;...}: 有对应属性的对应标签使用此样式
            例:
                a[class] {color:red} /*拥有class属性的a标签使用此样式*/
                a[class="123"] {color:blue} /*class属性值为123的a标签使用此样式*/
        2.3 结构性伪类选择器
        2.4 状态伪类选择器
        2.5 其他伪类选择器
"""