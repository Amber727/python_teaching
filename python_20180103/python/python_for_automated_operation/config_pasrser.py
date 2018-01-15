#!/usr/bin/python
# -*- coding:utf-8 -*-
import ConfigParser

cf = ConfigParser.ConfigParser(allow_no_value=True)
cf.read('my.cnf')    #读入配置文件内容

'''
# 查询配置文件内容
cf.sections()
cf.has_section('client')
cf.options('client')
cf.has_option('client', 'user')
cf.get('client', 'host')
cf.getint('client', 'port')
'''

# 修改配置文件内容
cf.remove_section('client')
cf.add_section('mysql')
cf.set('mysql', 'host', '127.0.0.1')
cf.set('mysql', 'port', 3306)
cf.write(open('my_copy.cnf', 'w'))
