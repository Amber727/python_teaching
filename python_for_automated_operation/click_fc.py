#!/usr/bin/python
# -*- coding:utf-8 -*-
'''在vi编辑器中编辑较长的命令，然后运行'''
from __future__ import print_function
import click
import os

message = click.edit()
print(message, end="")
os.system(message)
