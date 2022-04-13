import pytest
from database.database_object import Database
from models.AttackMoves import AttackMoves, SpaceAlreadyAttackedException
from models.Board import Board
from models.Game import Game
from tests.fixtures import constructed_database, add_default_boards, add_default_game, add_example_board


class TestAttackMoves:

    def test_attack(self, constructed_database, add_default_game, add_default_boards, add_example_board):
        game = Game.get_by_id(1)
        board = Board.get_by_id(game.Board1)

        assert AttackMoves.attack(board, "B2").isAHit == False
        assert AttackMoves.attack(board, "G6").isAHit == False
        assert AttackMoves.attack(board, "J10").isAHit == False

        assert AttackMoves.attack(board, "B4").isAHit == True
        assert AttackMoves.attack(board, "E5").isAHit == True
        assert AttackMoves.attack(board, "E10").isAHit == True
        assert AttackMoves.attack(board, "J5").isAHit == True

        with pytest.raises(SpaceAlreadyAttackedException) as e:
            AttackMoves.attack(board, 'B2')
        with pytest.raises(SpaceAlreadyAttackedException) as e:
            AttackMoves.attack(board, 'E5')

        assert len(AttackMoves.get_by_board(board.id)) == 7