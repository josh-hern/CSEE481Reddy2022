import json

from controllers.BaseController import *
from controllers.GameController import *
from flask import request

# from controllers.BaseController import *

api = Blueprint('/api/', __name__)


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


# OwO tewst woute
@api.route('/api/')
def test():
    return 'hey uWu'


# Place Ship
# Params:
#   - 'code'(string): game code. will be "HARDWARE" for war board games. otherwise look like "MhMoRG"
#   - 'position'(string): origin point of position. leftmost or topmost piece of ship. A-J, 1-10. Looks like "A5", "J10"
#   - 'ship_type'(string): type of ship, lowercase. "carrier", "destroyer", "battleship", "submarine", "patrol boat"
#   - 'rotate'(bool): false for horizont, true for vert
#   - 'player'(string): name of player playing game. can not be the same as other player or will raise WhatTheFuckException
# Returns:
#   - (object) status
@api.route('/api/place_ship', methods=['POST'])
def add_ship_position():
    request_json = json.loads(request.get_json())
    new_board = place_ship(request_json['code'], request_json['position'], request_json['ship_type'], request_json['rotate'], request_json['player'])
    return json.dumps(new_board)

# start game
# Params:
#   - 'name'(string): name of player playing game
# Returns:
#   - (int) game code
@api.route('/api/start_game', methods=['POST'])
def start_new_game_route():
    request_json = request.get_json()
    response = start_new_game(request_json['name'])
    return json.dumps(response)

# start board game
# Params:
#   - 'name'(string): name of player playing game
# Returns:
#   - (int) game code. will always be "HARDWARE"
@api.route('/api/start_board_game', methods=['POST'])
def start_new_board_game_route():
    request_json = request.get_json()
    response = start_new_board_game(request_json['name'])
    return json.dumps(response)

# confirm setup
# not required to be called for game to start. just tells if the board is setup
# Params:
#   - 'code'(string): game code. will be "HARDWARE" for war board games. otherwise look like "MhMoRG"
#   - 'name'(string): name of player playing game. looks for board with this name
# Returns:
#   - (bool) isready
@api.route('/api/confirm_setup', methods=['POST'])
def confirm_setup_route():
    request_json = request.get_json()
    response = confirm_setup(request_json['code'], request_json['name'])
    return json.dumps(response)


# join from web
# Params:
#   - 'code'(string): game code. will look like "MhMoRG"
#   - 'name'(string): name of player playing game. looks for board with this name
# Returns:
#   - (object) status
@api.route('/api/join_from_web', methods=['POST'])
def join_from_web_route():
    request_json = request.get_json()
    response = join_from_web(request_json['code'], request_json['name'])
    return json.dumps(response)


# check game status
# Params: 
#   - 'code'(string): game code. will look like "MhMoRG"
#   - 'name'(string): name of player playing game. looks for board with this name
# Returns:
#   - (object) status
@api.route('/api/check_game_status', methods=['POST'])
def check_game_status_route():
    request_json = request.get_json()
    response = check_game_status(request_json['code'], request_json['name']);
    return json.dumps(response)

# Attack Space
# Params:
#   - 'code'(string): game code. will be "HARDWARE" for war board games. otherwise look like "MhMoRG"
#   - 'cell'(string): cell to attack. A-J, 1-10. Looks like "A5", "J10"
#   - 'name'(string): name of player playing game. can not be the same as other player or will raise WhatTheFuckException
# Returns:
#   - (object) status. If fails, will still return status with currentPlayer unchanged.
@api.route('/api/attack_space', methods=['POST'])
def attack_space_route():
    request_json = request.get_json()
    response = attack_ship(request_json['code'], request_json['name'], request_json['cell']);
    return json.dumps(response)


@api.route('/api/check_stats', methods=['POST'])
def check_stats_route():
    request_json = request.get_json()
    response = check_stats(request_json['name'])
    return json.dumps(response, default=str)
