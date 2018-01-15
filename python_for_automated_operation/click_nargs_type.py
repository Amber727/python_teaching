#!/usr/bin/python
# -*- coding:utf-8 -*-
import click
@click.command()
@click.option('--pos', nargs=2, type=float)  # nargs 参数个数；type 将把参数变为浮点数格式

def findme(pos):
    #click.echo('%s / %s' % pos)
    click.echo('{} / {}'.format(pos[0], pos[1]))

if __name__ == '__main__':
    findme()

# run "python click_nargs_type.py  --pos=1 2"
