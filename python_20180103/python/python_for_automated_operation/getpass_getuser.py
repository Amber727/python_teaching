#!/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
import getpass

#user = getpass.getuser() #获取到当前登录的用户名
user = raw_input('your username: ')
passwd = getpass.getpass('your password: ')
print(user, passwd)
print(type(user), type(passwd))
