import initialize_game
from controllers.BaseController import *
from flask import request

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
    player_id = initialize_game.battleship_game.add_ship_position(position_json)
    # allow_json = check_allowed(player_id)  # TODO remember to uncomment this when functions are written
    # return allow_json
    return position_json


@api.route('/check_allowed')
def check_allowed(player_id):
    if initialize_game.battleship_game.check_space_exists() and initialize_game.battleship_game.check_not_adjacent():
        return f'<div>{player_id}, True</div>'
    else:
        return f'<div>{player_id}, False</div>'
    pass
