#! /usr/bin/python3
# coding:utf8

from flask import Flask, make_response
import json

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/test/a')
# app.add_url_rule('/url', view_func=index)
def test_page_a():
    # status code 200 404 301
    # content-type http headers
    # content-type = text/html
    # Response
    headers = {
        'content-type': 'application/json',
        'location': 'https://www.bing.com'
    }
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response


@app.route('/test/b')
# app.add_url_rule('/url', view_func=index)
def test_page_b():
    # status code 200 404 301
    # content-type http headers
    # content-type = text/html
    # Response
    headers = {
        'content-type': 'application/json',
        'location': 'https://www.bing.com'
    }
    return '<html></html>', 301, headers


@app.route('/admin')
def admin_index():
    return 'admin page'


@app.route('/api/test')
def api_test():
    data = {'name': 'jerry', 'age': 18}
    return json.dumps(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8000)
