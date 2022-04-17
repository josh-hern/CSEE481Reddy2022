import json

from controllers.BaseController import *
from controllers.GameController import *
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


@api.route('/api/place_ship', methods=['POST'])
def add_ship_position():
    request_json = json.loads(request.get_json())
    new_board = place_ship(request_json['code'], request_json['position'], request_json['ship_type'], request_json['rotate'], request_json['player'])
    return json.dumps(new_board)


@api.route('/api/start_game', methods=['POST'])
def start_new_game_route():
    request_json = request.get_json()
    response = start_new_game(request_json['name'])
    return json.dumps(response)


@api.route('/api/confirm_setup', methods=['POST'])
def confirm_setup_route():
    request_json = request.get_json()
    response = confirm_setup(request_json['code'], request_json['name'])
    return json.dumps(response)


@api.route('/api/join_from_warboard', methods=['POST'])
def join_from_war_board_route():
    pass


@api.route('/api/join_from_web', methods=['POST'])
def join_from_web_route():
    request_json = request.get_json()
    response = join_from_web(request_json['code'], request_json['name'])
    return json.dumps(response)


@api.route('/api/check_game_status', methods=['POST'])
def check_game_status_route():
    request_json = request.get_json()
    response = check_game_status(request_json['code'], request_json['name']);
    return json.dumps(response)


@api.route('/api/attack_space', methods=['POST'])
def attack_space_route():
    request_json = request.get_json()
    response = attack_ship(request_json['code'], request_json['name'], request_json['cell']);
    return json.dumps(response)


