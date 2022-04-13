import pytest
from database.database_object import Database
from models.Board import Board
from models.Game import Game
from models.OccupiedSpaces import SpaceAlreadyOccupiedException, OccupiedSpaces
from models.Player import Player
from models.Ship import Ship, InvalidShipNameException
from tests.fixtures import constructed_database, add_default_boards, add_default_game, add_default_ship


class TestShip:

    def test_place_ship(self, constructed_database, add_default_game, add_default_boards):
        game = Game.get_by_id(1)
        board = Board.get_by_id(game.Board1)

        assert Ship.add_ship(game.id, "destroyer", board, "A5", False)
        assert Ship.add_ship(game.id, "patrol boat", board, "C5", True)

        tmp = OccupiedSpaces.get_by_board(board.id)

        with pytest.raises(SpaceAlreadyOccupiedException) as e:
            Ship.add_ship(game.id, "patrol boat", board, "A5", False)
        with pytest.raises(SpaceAlreadyOccupiedException) as e:
            Ship.add_ship(game.id, "Submarine", board, "A4", False)
        with pytest.raises(SpaceAlreadyOccupiedException) as e:
            Ship.add_ship(game.id, "Submarine", board, "B5", False)
        with pytest.raises(InvalidShipNameException) as e:
            Ship.add_ship(game.id, "Little_Boat", board, "A3", False)

    def test_check_placement(self, constructed_database,add_default_game, add_default_boards, add_default_ship):
        ship = Ship.get_by_id(1)
        game = Game.get_by_id(1)
        board = Board.get_by_id(game.Board1)

        values = list(['H1', 'H2', 'H3', 'H4', 'H5'])
        assert Ship.check_placement(board, "H1", False, 5) == values

        values = list(['A2', 'B2'])
        assert Ship.check_placement(board, "A2", True, 2) == values

        with pytest.raises(SpaceAlreadyOccupiedException) as e:
            Ship.check_placement(board, "A5", False, 4)
