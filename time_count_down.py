#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import os
count = 0

a = input('time: ')
b = a * 60
while count < b:
    ncount = b - count
    os.system('clear')
    print ncount
    time.sleep(1)
    count += 1
print 'Done'
