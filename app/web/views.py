#! /usr/bin/python3
# coding:utf8

from . import web


@web.route("/")
def web_page():
    return '<h1>Hi,Welcome to home page...</h1>'
