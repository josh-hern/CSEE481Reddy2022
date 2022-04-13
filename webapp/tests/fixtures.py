import pytest
from database.database_object import Database
from models.Board import Board
from models.Game import Game
from models.Player import Player
from models.Ship import Ship


@pytest.fixture
def constructed_database(tmpdir):
    Database.create_engine(str(tmpdir), "database_test.db")
    Database.create_tables()


@pytest.fixture
def add_default_game():
    Game.create_game()


@pytest.fixture
def add_default_boards():
    game = Game.get_by_id(1)

    board1 = Board()
    board1.PlayerName = "Player1"
    board1.GameID = game.id
    Database.insert(board1)

    board2 = Board()
    board2.PlayerName = "Player2"
    board2.GameID = game.id
    Database.insert(board2)

    Game.update(game.id, {"Board1": 1, "Board2": 2})


@pytest.fixture
def add_default_ship():
    game = Game.get_by_id(1)
    board = Board.get_by_id(game.Board1)
    Ship.add_ship(game.id, "Carrier", board, "A5", False)

@pytest.fixture
def add_example_board():
    game = Game.get_by_id(1)
    board = Board.get_by_id(game.Board1)

    Ship.add_ship(game.id, "Battleship", board, "B4", False)
    Ship.add_ship(game.id, "Carrier", board, "D1", True)
    Ship.add_ship(game.id, "Destroyer", board, "E4", False)
    Ship.add_ship(game.id, "Patrol Boat", board, "D10", True)
    Ship.add_ship(game.id, "Submarine", board, "H5", True)