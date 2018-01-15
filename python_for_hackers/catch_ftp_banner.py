#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
    portList = [21,22,25,80,110,443]
    for x in range(110, 112):
        ip = '192.168.1.%d' % x
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print "{}: {}".format(ip, banner)

if __name__ == '__main__':
    main()
