"""
    异常:
        指运行期间检测到的错误, 如果产生的异常未被捕获处理, 程序会用所谓的回溯终止执行
        异常捕获语法:
            try:
                正常执行的代码
            except (异常类型,不填默认为所有异常类型均捕获):
                对异常的处理代码
        异常的传递:
            当函数/方法出现异常, 会将异常传递到函数/方法的调用一方, 当传递到主程序时, 如果还没有异常处理, 程序将被终止
        异常捕获完整语法:
            try:
                尝试执行的代码
                pass
            except 错误类型1:
                针对错误类型1做出的处理
                pass
            except (错误类型2, 错误类型3):
                针对错误类型2&3做出的处理
                pass
            # 捕获未知错误
            except Exception as result:
                # 打印错误信息
                print('未知错误{}'.format(result))
            else:
                # 没有异常才会执行的代码
                pass
            finally：
                # 无论是否有异常,都会执行的代码
                print('无论是否有异常,都会执行的代码！！')
        python的内建异常:
            1. Exception: 常规异常的基类
            2. IOError: 输入 / 输出操作失败
            3. KeyError: 映射中没有这个键
            4. SyntaxError: Python语法错误
            5. ValueError: 传入无效的参数
            6. AttributeError: 对象没有这个属性
            7. IndexError: 序列中没有此索引
            8. NameError: 未声明或初始化对象
            9. TypeError: 对类型无效的操作
            10 ZeroDivisionError: 除零(或取模0)异常
        主动抛出异常 ==> 自定义异常:
            python中提供了一个 Exception 异常类, 可以根据需求自定义异常
            a. 创建Exception对象
                exception_object = Exception('异常提示信息')
            b. 通过 raise 关键字抛出异常
                raise exception_object
"""