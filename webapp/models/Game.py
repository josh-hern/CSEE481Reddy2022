from sqlalchemy import ForeignKey, Column, String, Integer, DATETIME, Boolean
from database.base import Base
from database.database_object import Database
from models.BaseModel import BaseModel
from models.Board import Board
import datetime
import random, string


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
            game = session.query(cls).filter(cls.Code == code).first()

        return game