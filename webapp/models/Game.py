from sqlalchemy import ForeignKey, Column, String, Integer, DATETIME, Boolean
from database.base import Base
from database.database_object import Database
from models.BaseModel import BaseModel
from models.Board import Board
import datetime
import random, string

from models.Ship import Ship


class Game(Base, BaseModel):
    __tablename__ = "Game"

    Start = Column('Start', DATETIME)
    End = Column('End', DATETIME, nullable=True)
    Code = Column(String)
    isSetup = Column('isSetup', Boolean, default=False)
    CurrentTurn = Column(String, nullable=True)
    Board1 = Column(Integer, ForeignKey('Board.id'), nullable=True)
    Board2 = Column(Integer, ForeignKey('Board.id'), nullable=True)
    Winner = Column('Winner', String)

    @classmethod
    def create_game(cls, player_name = None):
        game = Game()
        game.Start = datetime.datetime.now()
        game.isSetup = False
        game.Code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        game = Database.insert(game)

        if player_name:
            board1 = Board.create_board(game.id, player_name)
            game = Game.update(game.id, {'Board1': board1.id})

        return game

    @classmethod
    def get_by_access_code(cls, code):
        game = None
        with Database.get_session() as session:
            game = session.query(cls).filter(cls.Code == code).order_by(cls.id.desc()).first()

        return game

    @classmethod
    def get_by_game_id(cls, game_id):
        game = None
        with Database.get_session() as session:
            game = session.query(cls).filter(cls.GameID == game_id).first()

        return game

    @classmethod
    def check_winner(cls, game_id):
        game = Game.get_by_id(game_id)
        board1 = Board.get_by_id(game.Board1)
        board2 = Board.get_by_id(game.Board2)

        ships1 = Ship.get_by_board(board1.id)
        alive1 = False
        for ship in ships1:
            if ship.isSunk is False:
                alive1 = True

        ships2 = Ship.get_by_board(board2.id)
        alive2 = False
        for ship in ships2:
            if ship.isSunk is False:
                alive2 = True

        if not alive1 or not alive2:
            game = Game.update(game.id, {"Winner": (board1.PlayerName if alive1 else board2.PlayerName)})
            return game

        else:
            return False
