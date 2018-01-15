#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import print_function
import os
import sys

def main():
    sys.argv.append('') #防止用户不传参数导致异常
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + " doesn't exist.")
    elif not os.access(filename, os.R_OK):
        raise SystemExit(filename + " is not accessible.")
    else:
        print(filename + " is accessible.")

if __name__ == '__main__':
    main()
