#!/usr/bin/python
# -*- coding:utf-8 -*-
import crypt
import fileinput
import sys
import time

def main():
    start_time = time.time()
    salt_db = {}
    password_db = {}
    
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = '/etc/shadow'
    
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip('\n')
            user = line.split(':',1)[0]
            password = line.split(':',2)[1]
            password_db[user] = password
            start_index = password.find('$')
            finish_index = password.rfind('$')
            if start_index != -1 :
                salt = password[start_index:finish_index+1]
                salt_db[user] = salt
    
#    for word in fileinput.input('dictionary.txt'):
#        word = word.strip('\n')
#        for user in salt_db.keys():
#            if crypt.crypt(word, salt_db[user]) == password_db[user]:
#                print '{}密码为：{}'.format(user,word)
#                del salt_db[user]
    i = 1
    with open('dictionary.txt') as f:
        for word in f:
            word = word.strip('\n')
            for user in salt_db.keys():
                if crypt.crypt(word, salt_db[user]) == password_db[user]:
                    print '{}密码为：{}'.format(user,word)
                    del salt_db[user]
                i += 1
    
    end_time = time.time()
    use_time = end_time - start_time
    print "\n用时：", use_time

if __name__ == '__main__':
    main()
