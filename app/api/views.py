#! /usr/bin/python3
# coding:utf8
from flask import jsonify
from . import api
import app.utils.ajax as ajax


@api.route('/')
def api_index():
    return '<h1>Welcome to json api page...</h1>'


@api.route('/user/info')
def user_info():
    data = {
        'name': 'jerry', 'age': 18
    }
    return jsonify(data)


@api.route('/district')
def api_district():
    ht = ajax.HTTP()
    headers = {
        'content-type': 'application/json'
    }
    result = ht.get('http://apis.juhe.cn/xzqh/query?fid=0')
    return result, 200, headers
