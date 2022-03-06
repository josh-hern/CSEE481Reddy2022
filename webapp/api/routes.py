from flask import Blueprint, render_template
from controllers.BaseController import *

api = Blueprint('/api/', __name__)

@api.route('/api/')
def test():
    return 'hey'

@api.route('/')
def homeRoute():
    return viewHome()
