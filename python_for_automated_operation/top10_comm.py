#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from collections import Counter
c = Counter()
path = os.path.expanduser('~')+'/.bash_history'

with open(path) as f:
    for line in f:
        com = line.split()[0]
        c[com] += 1
print "Top 10 commons is :"
for k,v in c.most_common(10):
    print "{}:\t{}".format(k,v)
