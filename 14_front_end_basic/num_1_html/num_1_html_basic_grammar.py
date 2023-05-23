"""
    HTML:
        是HyperText Mark-up Language的首字母简写, 即超文本标记语言
        超文本:
            1. 网页中可以显示图片、视频、音频等(超越文本限制)
            2. 可以从一个网页跳转到另一个网页, 与世界各地主机的网页链接(超链接文本)
        标记:
            指的是标签 ==> <标签名称></标签名称>, 比如<html></html>,<h1></h1>等, 标签大多数是成对出现的
        HTML是一种用来制作网页的语言, 这种语言由一个个的标签组成
    HTML基本结构:
        HTML是由标签和内容构成的
        标签语法: html中的标签是由<和>括起来的
        标签分类:
            1. 双标签: <标签名>....</标签名>
            2. 单标签: <标签名/>
        标签添加属性:
            <标签名 属性名1="值1" 属性名2="值2"...>...</标签名>
        标签规范:
            标签名小写, 属性值使用双引号, 标签要闭合, 多个属性之间用空格分开
        注释格式:
            <!-- 注释内容 -->
        基本结构:
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    各种页头属性设置, CSS样式和JavaScript脚本等
                </head>
                <body>
                    网页显示内容
                </body>
            </html>
    HTML 资源路径:
        分为绝对路径和相对路径:
        1. 绝对路径是从根目录算起的路径
        2. 相对路径是从当前目录算起的路径
"""