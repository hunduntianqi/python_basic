"""
    邮件发送任意类型附件
"""
# 导入smtplib模块
import smtplib
# 导入MIMEMultipart类, 用于创建邮件对象
from email.mime.multipart import MIMEMultipart
# 导入MIMEText类, 用于构建文本数据
from email.mime.text import MIMEText
# 导入Header类, 用于构建邮件主题信息
from email.header import Header

if __name__ == '__main__':
    # 创建smtplib连接对象
    smtp_conn = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # 登录邮箱
    smtp_conn.login('1729992141@qq.com', 'mhlvqczdayvfdcha')
    # 创建邮件对象
    msg = MIMEMultipart()
    # 构建邮件主题
    msg['Subject'] = Header('邮件发送文本附件测试程序')
    # 设置邮件发送人
    msg['From'] = '1729992141@qq.com <1729992141@qq.com>'
    # 设置邮件接收人群组
    list_recv: list = ['1729992141@qq.com', '2360199712@qq.com']
    msg['To'] = ';'.join(list_recv)
    # 准备文件附件
    file_content = open(r'D:\文件\java教程2021\3、Java入门到起飞（含斯坦福大学练习题+力扣算法题+'
                        r'大厂java面试题）\Java基础-视频\day01-Java入门\01-Java学习介绍.mp4', 'rb').read()
    text_object = MIMEText(file_content, 'base64', 'utf-8')
    text_object['Content-Disposition'] = 'attachment;filename="JavaStudy.mp4"'
    # 文本数据添加邮件对象
    msg.attach(text_object)
    # 发送邮件
    smtp_conn.sendmail('1729992141@qq.com', list_recv, msg.as_string())
    # 退出邮件服务器
    smtp_conn.quit()
