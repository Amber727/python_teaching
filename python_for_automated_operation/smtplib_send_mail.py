#!/usr/bin/python
# -*- coding:utf-8 -*-
import smtplib
import string
import getpass

HOST = 'smtp.126.com'
SUBJECT = 'Test email from Python'
TO = '724639089@qq.com'
FROM = 'liuyingshan727@126.com'
text = 'Amber is so handsome.'
BODY =  string.join((
        "FROM: %s" % FROM,
        "TO: %s" % TO,
        "SUBJECT: %s" % SUBJECT,
        "",
        text
        ),"\r\n")

PASSWORD = getpass.getpass("邮箱密码：")

server = smtplib.SMTP()     #创建一个SMTP对象
server.connect(HOST, '25')  #连接SMTP服务器
server.starttls()   #启用TLS安全传输模式，说有SMTP指令都将加密传输
server.login(FROM, PASSWORD)
server.sendmail(FROM, TO, BODY)     #发送邮件，参数依次为：发件人、收件人、邮件内容
server.quit()   #断开smtp服务器的连接
