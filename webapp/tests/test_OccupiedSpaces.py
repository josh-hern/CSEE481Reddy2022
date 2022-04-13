import pytest
from database.database_object import Database
from models.Board import Board
from models.Game import Game
from models.OccupiedSpaces import OccupiedSpaces, InvalidSpaceException, SpaceAlreadyOccupiedException
from models.Ship import Ship
from tests.fixtures import constructed_database, add_default_boards, add_default_game, add_default_ship


class TestOccupiedSpaces:

    def test_validity(self, constructed_database, add_default_game, add_default_boards, add_default_ship):
        game = Game.get_by_id(1)
        ship = Ship.get_by_id(1)
        board = Board.get_by_id(game.Board1)

        with pytest.raises(InvalidSpaceException) as e:
            OccupiedSpaces.check_validity('A11', board)
        with pytest.raises(InvalidSpaceException) as e:
            OccupiedSpaces.check_validity('A0', board)
        with pytest.raises(InvalidSpaceException) as e:
            OccupiedSpaces.check_validity('K1', board)
        with pytest.raises(InvalidSpaceException) as e:
            OccupiedSpaces.check_validity('V10', board)

        with pytest.raises(SpaceAlreadyOccupiedException) as e:
            OccupiedSpaces.check_validity('A5', board)
        with pytest.raises(SpaceAlreadyOccupiedException) as e:
            OccupiedSpaces.check_validity('B5', board)
        with pytest.raises(SpaceAlreadyOccupiedException) as e:
            OccupiedSpaces.check_validity('A6', board)
        with pytest.raises(SpaceAlreadyOccupiedException) as e:
            OccupiedSpaces.check_validity('A8', board)

        assert OccupiedSpaces.check_validity('A1', board)
        assert OccupiedSpaces.check_validity('J10', board)
        assert OccupiedSpaces.check_validity('D10', board)
        assert OccupiedSpaces.check_validity('J5', board)
        assert OccupiedSpaces.check_validity('D2', board)

    def test_get_by_board_id(self, constructed_database, add_default_game, add_default_boards, add_default_ship):
        game = Game.get_by_id(1)
        board = Board.get_by_id(game.Board1)
        spaces = OccupiedSpaces.get_by_board(board.id)

        assert spaces

        board = Board.get_by_id(game.Board2)
        spaces = OccupiedSpaces.get_by_board(board.id)

        assert not spaces