#! /usr/bin/python3
# coding:utf8
import requests


# 经典类和新式类

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        url = url + '&key=' + '6ad456ef1a60be17cfa3183932f104df'
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

    @staticmethod
    def post():
        pass
