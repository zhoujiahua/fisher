#! /usr/bin/python3
# coding:utf8
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.debug = app.config['DEBUG']

from app.web import web as web_blueprint
from app.admin import admin as admin_blueprint
from app.api import api as api_blueprint

app.register_blueprint(web_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(api_blueprint, url_prefix='/api')
