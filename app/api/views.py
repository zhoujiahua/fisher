#! /usr/bin/python3
# coding:utf8
from flask import request, jsonify
from . import api
from app.utils.ajax import HTTP
from app.forms.api import SearchForm


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
    ht = HTTP()
    headers = {
        'content-type': 'application/json'
    }
    result = ht.get('http://apis.juhe.cn/xzqh/query?fid=0')
    return result, 200, headers


@api.route('/search')
def api_search():
    key = request.args['key']
    page = request.args['page']
    data = {'key': key, 'page': page}
    return jsonify(data)


@api.route('/search/list')
def api_search_list():
    form = SearchForm(request.args)
    ht = HTTP()
    if form.validate():
        key = form.key.data.strip()
        page = form.page.data
        res = ht.get('http://apis.juhe.cn/xzqh/query?fid=' + key)
        result = {'key': key, 'page': page, 'data': res}
        return jsonify(result)
    else:
        return jsonify(form.errors)
