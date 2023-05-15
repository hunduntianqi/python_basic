"""
    MySql远程连接设置:
        1. 登录MySql:
            命令行窗口中 ==> mysql -u用户名 -p密码
        2. 进入mysql库:
            use mysql; ==> 切换数据库到mysql
        3. 执行更新权限语句:
            update user set Host='%' where User='root'; ==> '%'指的是所有地址
        4. 查看权限: select host, user from user; 查看权限
        5. 使用数据库连接工具测试连接
        个人电脑 ipv6 地址 ==> fe80::6504:9c14:bfcd:c535
        个人电脑宿舍WiFi ipv4 地址 ==> 192.168.16.101
        个人电脑 ==> GPT-HunDunTianQi
        idea ipv6 连接 mysql ==> 主机 = ipv6地址
    无管理员权限安装MySQL服务:
        1. 配置环境:
            mysql bin文件夹目录下, 创建.ini文件, 内容如下:
                [client]
                port=3306
                [mysqld]
                character-set-server=utf8
                [mysql]
                default-character-set=utf8
        2. 初始化:
            bin文件夹目录下, cmd命令行窗口输入命令: mysqld --initialize
            或 {MySql}\\bin\\mysqld --initialize
        3. 运行服务:
            bin文件夹目录下, cmd命令行窗口输入命令: mysqld --console
            或 {MySql}\\bin\\mysqld --console
        4. 查看密码:
            在MySQL data文件夹下以.err结尾的文件中[Note]一行的结尾
        5. 登录MySQL服务 ==> mysql -u用户名 -p密码
        6. 修改密码 ==> set password for 用户名@localhost = password('新密码');
"""
