#! /usr/bin/python3
# coding:utf8

from flask import Blueprint

api = Blueprint('api', __name__)
import app.api.views
