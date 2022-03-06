from flask import Blueprint, render_template
from controllers.BaseController import *

api = Blueprint('/api/', __name__)

@api.route('/api/')
def test():
    return 'hey uWu'

@api.route('/')
def homeRoute():
    return viewHome()

@api.route('/about')
def aboutRoute():
    return viewAbout()

@api.route('/history')
def historyRoute():
    return viewHistory()

@api.route('/merch')
def merchRoute():
    return viewMerch()
