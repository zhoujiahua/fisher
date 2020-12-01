#! /usr/bin/python3
# coding:utf8

from flask import Blueprint

web = Blueprint('web', __name__)
import app.web.views
