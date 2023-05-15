"""
    发送图片
"""
# 导入smtplib模块, 用于登录邮箱, 发送邮件
import smtplib
# 导入MIMEMultipart类, 用于组织邮件数据
from email.mime.multipart import MIMEMultipart
# 导入Header类, 用于设置邮件主题
from email.header import Header
# 导入MIMEText类, 用于构建文本内容
from email.mime.text import MIMEText
# 导入MIMEImage类, 用于构建文件附件
from email.mime.image import MIMEImage


# 定义函数, 邮件以附件形式发送图片
def send_pic_attachment():
    # 创建邮箱服务器连接对象
    qq_email = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # 登录邮箱
    qq_email.login('1729992141@qq.com', 'mhlvqczdayvfdcha')
    # 创建邮件对象
    msg = MIMEMultipart()
    # 设置邮件主题
    msg['Subject'] = Header('你好, 这是一个邮件发送图片测试程序').encode()
    # 设置发件人账号信息
    msg['From'] = '1729992141@qq.com<1729992141@qq.com>'
    # 设置邮件接收人信息
    list_recv = ['1729992141@qq.com', '2360199712@qq.com']
    msg['To'] = ';'.join(list_recv)
    # 构建文本内容 ==> 图片提示信息
    content = '美女图片\n'
    text = MIMEText(content, 'plain', 'utf-8')
    # 文本内容添加邮件对象
    msg.attach(text)
    # 构建图片附件 ==> 创建MIMEImage对象
    pic_data = open(r'D:\Users\Administrator\Pictures\Pic\pickure\he2udww1soz.jpg', 'rb').read()
    image = MIMEImage(pic_data)
    # 设置图片名字
    image['Content-Disposition'] = 'attach;filename=("he2udww1soz.jpg")'
    # 将图片附件添加进邮件对象
    msg.attach(image)
    # 发送邮件
    qq_email.sendmail(from_addr='1729992141@qq.com', to_addrs=list_recv, msg=msg.as_string())
    # 退出服务器
    qq_email.quit()


# 定义函数, 邮件以内容形式发送图片
def send_pic_content():
    # 创建邮箱服务器连接对象
    qq_email = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # 登录邮箱
    qq_email.login('1729992141@qq.com', 'mhlvqczdayvfdcha')
    # 创建邮件对象
    msg = MIMEMultipart()
    # 设置邮件主题
    msg['Subject'] = Header('你好, 这是一个邮件发送图片测试程序').encode()
    # 设置发件人账号信息
    msg['From'] = '1729992141@qq.com<1729992141@qq.com>'
    # 设置邮件接收人信息
    list_recv = ['1729992141@qq.com', '2360199712@qq.com']
    msg['To'] = ';'.join(list_recv)
    # 构建文本内容 ==> 图片提示信息, 并以html形式发送图片
    # 准备图片数据
    image_data = open(
        r'D:\Users\Administrator\Pictures\Pic\pickure\52314940016903763421664901429983.jpg', 'rb').read()
    # 创建图片对象
    image = MIMEImage(image_data)
    # 图片ID赋值 ==> image_object.add_header('Content-ID', '<自定义ID>')
    image.add_header('Content-ID', '<image1>')
    # 图片添加邮件对象
    msg.attach(image)
    # html内容显示图片固定写法 ==> <img src="cid:自定义图片ID">
    content = '''
    <美女图片>
    <br>
    <p>html显示图片测试</p>
    <img src="cid:image1">
    '''
    text = MIMEText(content, 'html', 'utf-8')
    # 文本内容添加邮件对象
    msg.attach(text)
    # 发送邮件
    qq_email.sendmail(from_addr='1729992141@qq.com', to_addrs=list_recv, msg=msg.as_string())
    # 退出服务器
    qq_email.quit()


if __name__ == '__main__':
    send_pic_content()
