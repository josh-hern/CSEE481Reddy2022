from flask import Blueprint, render_template

api = Blueprint('/api/', __name__)

@api.route('/api/')
def test():
    return 'hey'

@api.route('/')
def homeRoute():
    return render_template('index.html', test=test())
