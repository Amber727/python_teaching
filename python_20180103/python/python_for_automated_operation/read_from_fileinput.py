#!/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
import fileinput

for line in fileinput.input():
    print(line, end="")
