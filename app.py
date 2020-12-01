#! /usr/bin/python3
# coding:utf8

from flask import Flask, make_response
import json

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/book/serach')
def search():
    pass


@app.route('/admin')
def admin_index():
    return 'admin page'


@app.route('/api/test')
def api_test():
    data = {'name': 'jerry', 'age': 18}
    return json.dumps(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8000)
