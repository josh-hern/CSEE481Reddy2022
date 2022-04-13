import pytest
from controllers.GameController import *
from models.Game import Game
from models.OccupiedSpaces import SpaceAlreadyOccupiedException
from models.Ship import ShipAlreadyPlacedException
from tests.fixtures import constructed_database, add_default_boards, add_default_game


class TestGame:

    def test_start_new_game(self, constructed_database):
        games = Game.get_all()
        assert not games

        game = start_new_game("Bingo")
        assert game

        game = start_new_game("Bingus")
        assert game

        games = Game.get_all()
        assert len(games) == 2

    def test_place_ship(self, constructed_database, add_default_game, add_default_boards):
        game = Game.get_by_id(1)
        board = Board.get_by_id(game.Board1)

        assert place_ship(game.Code, "A1", "Carrier", False, board.PlayerName)

        with pytest.raises(SpaceAlreadyOccupiedException) as e:
            place_ship(game.Code, "B1", "Carrier", False, board.PlayerName)

        with pytest.raises(WhatTheFuckException) as e:
            place_ship(game.Code, "B1", "Carrier", False, "Dingo")

        with pytest.raises(ShipAlreadyPlacedException) as e:
            place_ship(game.Code, "D1", "Carrier", False, board.PlayerName)

        assert place_ship(game.Code, "E1", "Destroyer", False, board.PlayerName)

        assert len(Ship.get_by_board(board.id)) == 2
