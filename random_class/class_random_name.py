#!/usr/bin/python
# -*- coding:utf-8 -*-
# 随机抽取学生姓名
import random
import os
import time
os.system('clear')
ClassNum = raw_input('输入班号：')
a = '{}.txt'.format(ClassNum)
time.sleep(0.1)

def OpenFile(filename):
    with open(filename) as f:
        l = f.readlines()
    return l

while True:
    try:
        li = OpenFile(a)
        random.shuffle(li)
        print li[0],
        time.sleep(0.1)
        os.system('clear')
    except KeyboardInterrupt:
        print '^    恭喜！'
        exit()
