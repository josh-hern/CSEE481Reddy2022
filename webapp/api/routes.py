from flask import request

# from webapp.app import battleship_game
from webapp.controllers.BaseController import *

# from controllers.BaseController import *

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


@api.route('/add_ship_position', methods=['POST'])
def add_ship_position():
    position_json = request.get_json()
    print(position_json)
    # battleship_game.add_ship_position(position_json)
    return position_json
