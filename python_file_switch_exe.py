"""
    python文件打包成可执行EXE文件:
        1. 安装pyinstaller
            pip install pyinstaller
        2. 打包命令
            在python文件同级目录下:
                a. pyinstaller -F python_file_name.py ==> 默认打包exe命令
                b. pyinstaller -F -w python_file_name.py ==> 不带控制台的打包
                c. pyinstaller -F -i xx.ico python_file_name.py ==> 指定logo打包
    通过pipenv模块减小EXE文件大小:
        1. 安装pipenv模块 ==> pip install pipenv
        2. 创建虚拟环境 ==> 随便找个文件夹(最好路径是全英文), 命令行窗口 ==> pipenv install
        3. 进入虚拟环境 ==> pipenv shell
        4. 安装需要的模块 ==> pip install module1 module2 ...
        5. 安装 pyinstaller, 否则还会用系统中原来的 pyinstaller 打包
        6. 打包python文件, 将要打包的python文件复制到虚拟环境文件夹中, 使用虚拟环境的pyinstaller打包
        pipenv常用命令:
            pipenv --venv ==> 列出虚拟环境路径
            pipenv install --python xx ==> 初始化虚拟环境, 指定python版本, --python xx为可选参数
            pipenv shell ==> 进入虚拟环境
            pipenv uninstall --all ==> 卸载所有包
            pipenv uninstall 包名 ==> 删除部分包
            pipenv --rm ==> 删除虚拟环境
"""