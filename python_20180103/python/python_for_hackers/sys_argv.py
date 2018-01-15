#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import fileinput
import time

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print "Rreding from", filename, "..."
        time.sleep(1)
    
        if os.path.isfile(filename):
            for line in fileinput.input(filename):
                print line,
        else:
            print 'Error: The {} is does not exist.'.format(filename)

if __name__ == '__main__':
    main()
