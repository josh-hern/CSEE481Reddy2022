import pytest
from database.database_object import Database
from models.Board import Board
from models.Game import Game
from models.Player import Player
from models.Ship import Ship

from controllers.GameController import *


@pytest.fixture
def constructed_database(tmpdir):
    Database.create_engine(str(tmpdir), "database_test.db")
    Database.create_tables()


@pytest.fixture
def add_default_game():
    Game.create_game()


@pytest.fixture
def add_default_boards():
    private_add_board1()
    private_add_board2()


@pytest.fixture
def add_board1():
    private_add_board1()


def private_add_board1():
    game = Game.get_by_id(1)

    board = Board()
    board.PlayerName = "Player1"
    board.GameID = game.id
    board = Database.insert(board)

    Game.update(game.id, {"Board1": board.id})

    return board


@pytest.fixture
def add_board2():
    private_add_board2()


def private_add_board2():
    game = Game.get_by_id(1)

    board = Board()
    board.PlayerName = "Player2"
    board.GameID = game.id
    board = Database.insert(board)

    Game.update(game.id, {"Board2": board.id})

    return board

@pytest.fixture
def add_default_ship():
    game = Game.get_by_id(1)
    board = Board.get_by_id(game.Board1)
    Ship.add_ship(game.id, "Carrier", board, "A5", False)


@pytest.fixture
def add_example_board():
    private_add_example_board()


def private_add_example_board():
    game = Game.get_by_id(1)
    board = Board.get_by_id(game.Board1)

    add_some_ships(board, game)


@pytest.fixture
def add_example_board2():
    private_add_example_board()


def private_add_example_board2():
    game = Game.get_by_id(1)
    board = Board.get_by_id(game.Board2)

    add_some_ships(board, game)


def add_some_ships(board, game):
    Ship.add_ship(game.id, "Battleship", board, "B4", False)
    Ship.add_ship(game.id, "Carrier", board, "D1", True)
    Ship.add_ship(game.id, "Destroyer", board, "E4", False)
    Ship.add_ship(game.id, "Patrol Boat", board, "D10", True)
    Ship.add_ship(game.id, "Submarine", board, "H5", True)
    confirm_setup(game.Code, board.PlayerName)