import requests, schedule, time
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def data():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = 'http://www.weather.com.cn/weather/101180106.shtml'
    res = requests.get(url, headers=headers)
    print(res.status_code)
    res.encoding = 'utf-8'
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    wendu = soup.find(class_="tem").text
    tianqi = soup.find(class_="wea").text
    return wendu, tianqi


def send_email(wendu, tianqi):
    host = "smtp.qq.com"
    # port变量代表的是端口，这里使用SMTP服务器默认的端口号25，因为下面用的是smtplib.SMTP()未加密的方法
    port = 465
    # username变量代表的是登录邮箱的用户名
    username = '1729992141@qq.com'
    # password变量代表的是授权码，切记你的授权码之间一定不要有空格，否则会报错，告诉你验证失败。
    password = "mhlvqczdayvfdcha"
    # 邮件发送地址也就是上面你的username（登录邮箱的用户名）
    from_addr = username
    # 邮件收件人地址
    to_addr = ['1729992141@qq.com', '2360199712@qq.com', '17320101759@189.cn', 'hunduntianqi@qq.com']

    text = '河南省郑州市新郑市今天的天气是:\n' + wendu + tianqi
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(','.join(to_addr))
    msg['Subject'] = Header('收件好：')
    # 调用发送邮件模块下面的SMTP邮件传输协议这个类，并赋值给server这个变量，方便后面使用
    server = smtplib.SMTP_SSL(host)
    # 用connect(host, port)方法去连接邮箱的服务器
    server.connect(host, port)
    # 用login(username, password)去登陆邮箱服务器
    server.login(username, password)
    # 用sendmail(sender, to_addr, msg.as_string())去写邮件的发件人和收件人以及收件内容并发送邮件
    # msg.as_string()方法是指发送邮件的内容为一个字符串类型
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 退出服务器，结束SMTP会话
    server.quit()


def weither():
    wendu, tianqi = data()
    send_email(wendu, tianqi)


schedule.every().day.at('19:22').do(weither)
while True:
    schedule.run_pending()
    time.sleep(1)
