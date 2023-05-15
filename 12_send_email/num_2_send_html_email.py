"""
    发送HTML内容的邮件
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
    qq_email.login('1729992141@qq.com', 'mhlvqczdayvfdcha')
    # 创建邮件对象
    msg = MIMEMultipart()
    # 设置邮件主题
    msg['Subject'] = Header('你好, 这是一个邮件发送html测试程序').encode()
    # 设置发件人账号信息
    msg['From'] = '1729992141@qq.com<1729992141@qq.com>'
    # 设置邮件接收人信息
    list_recv = ['1729992141@qq.com', '2360199712@qq.com']
    msg['To'] = ';'.join(list_recv)
    # 构建文本内容 ==> HTML文本
    content = '''
    <h1>python email send to test!!</h1>
    <h1>python email send to test!!</h1>
    <h2>python email send to test!!</h2>
    <h3>python email send to test!!</h3>
    <h4>python email send to test!!</h4>
    <h5>python email send to test!!</h5>
    <h6>python email send to test!!</h6>
    <img src="https://img.5mtb.com/c2022/03/17/he2udww1soz.jpg">
    <br>
    <a href="https://www.baidu.com">点击跳转百度首页</a>
    '''
    text = MIMEText(content, 'html', 'utf-8')
    # 文本内容添加邮件对象
    msg.attach(text)
    # 发送邮件
    qq_email.sendmail(from_addr='1729992141@qq.com', to_addrs=list_recv, msg=msg.as_string())
    # 退出服务器
    qq_email.quit()
