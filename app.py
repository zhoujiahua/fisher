#! /usr/bin/python3
from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/api/test')
def api_test():
    data = {'name': 'jerry', 'age': 18}
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
