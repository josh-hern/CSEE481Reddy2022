import pytest
from database.database_object import Database
from models.Game import Game
from models.Player import Player
from tests.fixtures import constructed_database, add_default_boards, add_example_board2, add_example_board, add_default_game


class TestGame:

    def test_create_game(self, constructed_database):
        games = Game.get_all()
        assert not games

        game = Game.create_game()
        assert game

        games = Game.get_all()
        assert games

    def test_get_by_access_code(self, constructed_database, add_default_game):
        game = Game.get_by_id(1)
        code = game.Code

        assert game.id == Game.get_by_access_code(code).id

    def test_check_winner(self, constructed_database, add_default_game, add_default_boards, add_example_board):
        game = Game.get_by_id(1)
        game.check_winner(game.id)