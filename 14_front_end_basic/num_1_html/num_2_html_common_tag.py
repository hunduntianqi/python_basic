"""
    文本标签:
        1. <hn>...</hn>: n为1-6的值, 标题标签(加粗, 独立一行)
        2. <i>...</i>: 斜体
        3. <em>...</em>: 强调斜体
        4. <b>...</b>: 加粗
        5. <strong>...</strong>: 强调加粗
        6. <cite>...</cite>: 作品的标题(引用)
        7. <sub>...</sub>: 下标
        8. <sup>...</sup>: 上标
        9. <del>...</del>: 删除线
        10. <u>...</u>: 添加下划线
    格式化标签
        1. <br/>: 换行
        2. <p>...</p>: 换段
        3. <hr/>: 水平分割线
        4. 列表:
            4.1 <ul>...</ul>: 无序列表
            4.2 <ol>...</ol>: 有序列表
            4.3 <li>...</li>: 列表项
            4.4 <dl>...</dl>: 自定义列表
            4.5 <dt>...</dt>: 自定义列表头
            4.6 <dd>...</dd>: 自定义列表内容
        5. <div>...</div>: 块标签, 常用于组合块级元素, 以便通过CSS来对元素进行格式化
        6. <span>...</span>: 常用于包含的文本, 可以通过CSS对他定义样式, 或者使用JavaScript对他进行操作
    图片标签:
        <img/>: 在网页中插入一张图片
        属性:
            1. src: 图片名以及url地址
            2. alt: 图片加载失败时的提示信息
            3. title: 文字提示属性
            4. width: 图片宽度
            5. height: 图片高度
            6. border: 边框线粗细
    超链接标签:
        <a href="连接地址">...</a>: 超链接标签
        属性:
            1. href: 必须有, 指的是链接地址
            2. target: 表示连接的打开方式
                2.1 _blank: 新窗口
                2.2 _parent: 父窗口
                2.3 _self: 本窗口(默认)
                2.4 _top: 顶级窗口
                2.5 framenname: 窗口名
            3. title: 文字提示属性
        锚点链接:
            定义一个锚点: <a id="a1"></a>
            使用锚点: <a href="#a1">跳到a1处</a>
    表格标签:
        1. <table>...</table>: 表格标签,
            属性:
                border
                width
                cellspacing
                cellpadding
        2. <caption>...</caption>: 表格标题
        3. <tr>...</tr>: 行标签
        4. <th>...</th>: 列头标签
        5. <td>...</td>: 列标签
            跨行属性: rowspan
            跨列属性: colspan
        6. <thead>...</thead>: 表头
        7. <tbody>...</tbody>: 表体
        8. <tfoot>...</tfoot>: 表尾
    表单标签:
        1. form:表单标签
            action属性:设置表单数据提交地址
            method属性:设置表单提交的方式,一般有“GET”和“POST”方式,不区分大小写
        2. label:标记标签(通常和input标签一起使用)
        3. input:输入标签
            type属性:
                text-文本输入框
                password-密码输入框
                radio-单选框
                CheckBox-复选框
                file-上传文件
                submit-提交按钮
                reset-重置按钮
                date-日期
                color-选择颜色
            value属性:设定value值,用于网络间传输
            name属性:设定key值,用于网络间传输
            placeholder: 设置默认提示信息
        4. textarea:多行文本框
        5. select:下拉框
        6. option:选项框
        7. <fieldset>...</fieldset>: 将表单内的相关元素分组
        8. <legend>...</legend>: 为<fieldset>, <figure>和<details>元素定义标题
        9. <datalist>html5的标签</datalist>: 定义可选数据的列表
        10. <optgroup>html5标签</optgroup>: 定义选项组
        表单标签中:
            name属性: 设置表单元素的名称,该名称是提交数据时的参数名
            value属性:设置表单元素的值,该值是提交数据时参数名所对应的值
    行内框架标签:
        <iframe>...</iframe>:行内框架标签
            属性:
                src: 规定在iframe中显示的文档的url
                name: 规定iframe的名称
                height: 规定iframe的高度
                width: 定义iframe的宽度
                frameborder: 规定是否显示框架周围的边框
    多媒体标签:
        1. <audio>...</audio>: 音频标签
        2. <video>...</video>: 视频标签
        3. <embed/>: 播放Flash的标签

"""