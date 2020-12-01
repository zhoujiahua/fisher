#! /usr/bin/python3
# coding:utf8
from flask import jsonify
from . import api


@api.route('/')
def api_index():
    return '<h1>Welcome to json api page...</h1>'


@api.route('/user/info')
def user_info():
    data = {
        'name': 'jerry', 'age': 18
    }
    return jsonify(data)
