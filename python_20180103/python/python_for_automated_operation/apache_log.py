#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
分析apache访问日志
1.统计访问量最高的前5个页面
2.统计错误访问率
3.统计PV、UV
'''
from __future__ import print_function
from collections import Counter
import sys

pages = Counter()
ips = []
code = Counter()
error_requests = 0
sum_requests = 0
if len(sys.argv) >= 2:
    log_file = sys.argv[1]
else:
    log_file = '/var/log/apache2/access.log'

with open(log_file) as f:
    for line in f:
    #统计各个网页的浏览次数
        line = line.split()
        pages[line[6]] += 1     
    
    #统计PV、UV
        ips.append(line[0])

    #统计错误率
        key = line[8]
        code[key] += 1
    for k,v in code.iteritems():
        if int(k) >= 400:
            error_requests += v
        sum_requests += v

    
    try:
        print('Popular pages: {}'.format(pages.most_common(5)))
        print('Error rage: {:.2f}%'.format(error_requests * 100.0 / sum_requests))
        print('PV :{}\nUV: {}'.format(len(ips),len(set(ips))))
    except ZeroDivisionError,e:
        print('Error: ',e)
