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
    board = Board.create_board(game.id, player)

    
    Game.update(game.id, {"Board2": board.id})

    return True


def place_ship(game_code, position, ship_type, rotate, player):
    game = Game.get_by_access_code(game_code)
    board = None

    if Board.get_by_id(game.Board1).PlayerName == player:
        board = Board.get_by_id(game.Board1)

    elif Board.get_by_id(game.Board2).PlayerName == player:
        board = Board.get_by_id(game.Board2)

    else:
        raise WhatTheFuckException()

    test = Ship.add_ship(game, ship_type, board, position, rotate)

    current_board = OccupiedSpaces.get_by_board(board.id)
    spaces = list()

    for space in current_board:
        spaces.append(space.as_dict())
    return spaces


def confirm_setup(game_code, player):
    game = Game.get_by_access_code(game_code)
    board = None

    if Board.get_by_id(game.Board1).PlayerName == player:
        board = Board.get_by_id(game.Board1)

    elif Board.get_by_id(game.Board2).PlayerName == player:
        board = Board.get_by_id(game.Board2)

    else:
        raise WhatTheFuckException()

    if len(Ship.get_by_board(board.id)) == 5:
        Board.update(board.id, {"isSetup": True})
        return True
    else:
        return False
