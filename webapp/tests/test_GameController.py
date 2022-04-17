import pytest
from controllers.GameController import *
from models.Game import Game
from models.OccupiedSpaces import SpaceAlreadyOccupiedException
from models.Ship import ShipAlreadyPlacedException
from tests.fixtures import constructed_database, add_default_boards, add_default_game, add_board1, add_example_board, add_example_board2, private_add_example_board, private_add_example_board2


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

    def test_join_from_web(self, constructed_database, add_default_game, add_board1):
        game = Game.get_by_id(1)

        assert not join_from_web(game.Code, "Player1")
        assert join_from_web(game.Code, "subwayjared")
        assert join_from_web(game.Code, "Player1")

        assert not join_from_web(game.Code, "sneakypete")

    def test_get_board(self, constructed_database, add_default_game, add_default_boards):
        game = Game.get_by_id(1)

        assert get_board(game, "Player1").id == 1
        assert get_board(game, "Player2").id == 2

        with pytest.raises(WhatTheFuckException) as e:
            get_board(game, "sneakypete")

        assert get_enemy_board(game, "Player1").id == 2
        assert get_enemy_board(game, "Player2").id == 1

        with pytest.raises(WhatTheFuckException) as e:
            get_enemy_board(game, "sneakypete")

    def test_check_game_status(self, constructed_database, add_default_game, add_default_boards):
        game = Game.get_by_id(1)
        board = get_board(game, "Player1")

        assert not check_game_status(game.Code, board.PlayerName)['ready']
        assert not check_game_status(game.Code, board.PlayerName)['player-board']['isSetup']
        assert not check_game_status(game.Code, board.PlayerName)['enemy-board']['isSetup']

        private_add_example_board()

        assert not check_game_status(game.Code, board.PlayerName)['ready']
        assert check_game_status(game.Code, board.PlayerName)['player-board']['isSetup']
        assert not check_game_status(game.Code, board.PlayerName)['enemy-board']['isSetup']

        private_add_example_board2()

        assert check_game_status(game.Code, board.PlayerName)['ready']
        assert check_game_status(game.Code, board.PlayerName)['player-board']['isSetup']
        assert check_game_status(game.Code, board.PlayerName)['enemy-board']['isSetup']