"""
    发送邮件:
        smtplib模块 ==> python的邮件传输协议封装库
            1. 连接邮箱服务器, 创建smtplib对象
                smtplib_connect_object = smtplib.SMTP_SSL('smtp.email_type.com', server_port)
                email_type ==> 邮箱类型, QQ邮箱 ==> qq, 163邮箱 ==> 163
                smtp.email_type.com: 邮箱服务器地址
                server_port: 邮箱服务端口号, 465 / 25
            2. 登录用来发送邮件的邮箱
                smtplib_connect_object.login('email_account', 'password')
                password: 如果是qq邮箱, 需要使用邮箱授权码, 不能直接使用密码
            3. 准备邮件数据
                from email.mime.multipart import MIMEMultipart ==> 导入MIMEMultipart类, 用于
                组织邮件数据
                a. 创建邮件对象
                    msg = MIMEMultipart()
                b. 设置邮件主题
                    from email.header import Header ==> 导入Header类, 用于设置邮件主题
                    Subject = Header('主题信息', 编码方式).encode()
                    msg['Subject'] = Subject
                c. 设置发件人 ==> msg['From'] = '发送邮件账号'
                d. 设置收件人 ==> msg['TO'] = '收件人1账号;收件人2账号...'
                e. 构建邮件内容
                    1. from email.mime.text import MIMEText ==> 构建文本内容
                        text_object = MIMEText('文本内容', '文本类型', '编码方式')
                        文本类型:
                            plain ==> 普通文字
                            html ==> 超链接文本(网页形式, 是常见使用形式)
                            base64 ==> 二进制文件(一般对应于附件)
                        文本添加邮件对象中 ==> msg.attach(text)
                    2. from email.mime.image import MIMEImage ==> 构建图片附件
                        image_object = MIMEImage(图片二进制数据)
                        设置图片附件名:
                            image_object["Content-Disposition"] = "attachment;filename='文件名'"
                        图片附件添加到邮件对象中 ==> msg.attach(image_object)
            4. 发送邮件
                smtplib_connect_object.sendmain(发件人邮箱, 收件人邮箱序列, 字符串形式的邮件数据(msg.as_string()))
            5. 退出邮箱服务器
                smtplib_connect_object.quit()

"""
# 导入smtplib模块, 用于登录邮箱, 发送邮件
import smtplib
# 导入MIMEMultipart类, 用于组织邮件数据
from email.mime.multipart import MIMEMultipart
# 导入Header类, 用于设置邮件主题
from email.header import Header
# 导入MIMEText类, 用于构建文本内容
from email.mime.text import MIMEText

if __name__ == '__main__':
    # 创建邮箱服务器连接对象
    qq_email = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # 登录邮箱
    qq_email.login('1729992141@qq.com', 'kbxwniucpokcchgf')
    # 创建邮件对象
    msg = MIMEMultipart()
    # 设置邮件主题
    msg['Subject'] = Header('你好, 这是一个邮件发送文本测试程序').encode()
    # 设置发件人账号信息
    msg['From'] = '1729992141@qq.com<1729992141@qq.com>'
    # 设置邮件接收人信息
    list_recv = ['1729992141@qq.com', '2360199712@qq.com']
    msg['To'] = ';'.join(list_recv)
    # 构建文本内容 ==> 普通文本
    text = MIMEText('python smtplib send email test!!!', 'plain', 'utf-8')
    # 文本内容添加邮件对象
    msg.attach(text)
    # 发送邮件
    qq_email.sendmail(from_addr='1729992141@qq.com', to_addrs=list_recv, msg=msg.as_string())
    # 退出服务器
    qq_email.quit()
