"""
    CSS层叠样式表:
        定义如何显示控制HTML元素, 从而实现美化html页面, 多个样式定义可层叠为一, 后者可以覆盖前者样式
        CSS语法:
            格式:
                <style>
                    选择器{属性:值; 属性:值; 属性: 值...}
                </style>
                其中选择器也叫选择符
            例:
                P {color:red; text-align:center}
        CSS中的注释:
            /*...*/
        HTML中如何使用CSS样式:
            1. 内联方式(行内样式):
                指在html标签中使用style属性设置css样式
                特点: 仅对本标签有效
                格式: <html标签 style="属性:值;属性:值;..."></html标签>
                例: <p style="color:blue;font-family:隶书">在html中如何使用css样式</p>
            2. 内部方式(内嵌样式):
                在head标签中使用<style type="text/css">...</style>标签来设置css样式
                特点: 对当前的整个html页面有效
                格式:
                    <style type="text/css">
                        ...css样式代码
                    </style>
            3. 外部导入方式(外部链入):
                特点: 作用于当前整个网站
                3.1 使用link标签导入:
                    格式: <link href="文件名.css" type="text/css" rel="stylesheet"/>
                3.2 使用import在style标签中导入css文件:
                    <style type="text/css">
                        @import "style.css"
                    </style>
            优先级:
                1. 样式冲突时: 就近原则, 指css属性以距离最近的css样式为主
                2. 无样式冲突: 采用多样式修饰叠加的效果
        盒子模型:
            把HTMl页面的元素看作一个矩形盒子, 矩形盒子由
            内容(content), 内边距(padding), 边框(border), 外边距(margin)四部分组成
            相关样式属性:
                1. 盒子的内容宽度(width), 注意: 不是盒子的宽度
                2. 盒子的内容高度(height), 注意: 不是盒子的高度
                3. 盒子的边框(border)
                4. 盒子内的内容和边框之间的间距(padding)
                5. 盒子与盒子之间的间距(margin)
"""
