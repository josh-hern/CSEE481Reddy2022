import datetime
from datetime import datetime

import pytest
import os
from database.database_object import Database
from models.Board import Board
from models.Game import Game
from tests.fixtures import constructed_database, add_default_boards, add_default_game

from models.Player import Player
from models.Ship import Ship


class TestDatabase:
    def test_database(self, tmpdir):
        assert not os.path.isfile(os.path.join(tmpdir, "database_test.db"))

        Database.create_engine(str(tmpdir), "database_test.db")
        Database.create_tables()

        assert os.path.isfile(os.path.join(tmpdir, "database_test.db"))

    def test_create_players(self, constructed_database):
        players = Player.get_all()
        assert not players

        Player.create_default_players()
        players = Player.get_all()

        assert len(players) == 2

    def test_get_all(self, constructed_database, add_default_game, add_default_boards):
        board = Board.get_all()
        assert len(board) == 2

    def test_get_by_id(self, constructed_database, add_default_game):
        game = Game.get_by_id(0)
        assert not game

        game = Game.get_by_id(1)
        assert game

    def test_update(self, constructed_database, add_default_game, add_default_boards):
        game = Game.get_by_id(1)

        game = Game.update(game.id, {'isSetup': True})

        assert game.isSetup and game.updated_at
