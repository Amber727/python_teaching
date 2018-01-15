#!/usr/bin/python
# -*- coding:utf-8 -*-
import click

@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True) # prompt=True, 交互式输入密码；hide_input=True, 隐藏密码；confirmation_prompt=True, 两次验证

def encrypt(password):
    click.echo('Encryping password to {}'.format(password.encode('rot13')))  # encode('rot13') 使用rot13加密密码内容

encrypt()
