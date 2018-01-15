#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = 'app1.log'
)

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
