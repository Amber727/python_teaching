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

server = smtplib.SMTP()
server.connect(HOST, '25')
server.starttls()
server.login(FROM, PASSWORD)
server.sendmail(FROM, TO, BODY)
server.quit()
