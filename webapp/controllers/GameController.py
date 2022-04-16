from models.AttackMoves import AttackMoves
from models.BaseModel import WhatTheFuckException
from models.Game import Game
from models.OccupiedSpaces import OccupiedSpaces
from models.Ship import Ship
from models.Board import Board


def start_new_game(player1_name):
    game = Game.create_game(player1_name);
    return game.Code


def join_from_web(game_code, player):
    game = Game.get_by_access_code(game_code)
    if game.Board2 is None:
        board = Board.create_board(game.id, player)
        Game.update(game.id, {"Board2": board.id})
        return True

    else:
        raise WhatTheFuckException()


def get_board(game, player):
    board = None

    if Board.get_by_id(game.Board1).PlayerName == player:
        board = Board.get_by_id(game.Board1)

    elif Board.get_by_id(game.Board2).PlayerName == player:
        board = Board.get_by_id(game.Board2)

    else:
        raise WhatTheFuckException()

    return board


def get_enemy_board(game, player):
    board = None

    if Board.get_by_id(game.Board1).PlayerName == player:
        board = Board.get_by_id(game.Board2)

    elif Board.get_by_id(game.Board2).PlayerName == player:
        board = Board.get_by_id(game.Board1)

    else:
        raise WhatTheFuckException()

    return board


def place_ship(game_code, position, ship_type, rotate, player):
    game = Game.get_by_access_code(game_code)
    board = get_board(game, player)

    test = Ship.add_ship(game, ship_type, board, position, rotate)

    raw_spaces = OccupiedSpaces.get_by_board(board.id)
    return build_dict_list(raw_spaces)


def build_dict_list(raw_spaces):
    spaces = list()
    for space in raw_spaces:
        spaces.append(space.as_dict())
    return spaces


def confirm_setup(game_code, player):
    game = Game.get_by_access_code(game_code)
    board = get_board(game, player)

    if len(Ship.get_by_board(board.id)) == 5:
        Board.update(board.id, {"isSetup": True})
        return True
    else:
        return False


def check_game_status(game_code, player):
    game = Game.get_by_access_code(game_code)
    board = get_board(game, player)
    enemy_board = get_enemy_board(game, player)

    status = {
        'ready': board.isSetup and enemy_board.isSetup,
        'player-board': {
            'id': None,
            'isSetup': False,
            'occupied-spaces': list(),
            'ships': list()
        }, 'enemy-board': {
            'id': None,
            'isSetup': False,
            'attack-spaces': list(),
            'ships': list()
        }
    }

    status['player-board']['id'] = board.id
    status['player-board']['isSetup'] = board.isSetup
    status['player-board']['occupied-spaces'] = build_dict_list(OccupiedSpaces.get_by_board(board.id))
    status['player-board']['ships'] = build_dict_list(Ship.get_by_board(board.id))

    status['enemy-board']['id'] = enemy_board.id
    status['enemy-board']['isSetup'] = enemy_board.isSetup
    status['enemy-board']['attack-spaces'] = build_dict_list(AttackMoves.get_by_board(enemy_board.id))
    status['enemy-board']['ships'] = build_dict_list(Ship.get_by_board(enemy_board.id))

    return status
