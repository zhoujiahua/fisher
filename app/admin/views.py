#! /usr/bin/python3
# coding:utf8

from . import admin


@admin.route('/')
def admin_index():
    return 'Hi admin page'


@admin.route('/list')
def admin_list():
    return 'Hi admin list'


@admin.route('/detail')
def admin_detail():
    return 'Hi admin detail'
