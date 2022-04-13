from sqlalchemy import ForeignKey, Column, Integer, DATETIME, Boolean, String
from database.base import Base
from database.database_object import Database
from models.BaseModel import BaseModel


class Board(Base, BaseModel):
    __tablename__ = "Board"

    isSetup = Column('isSetup', Boolean, default=False)
    PlayerName = Column(String, nullable=False)
    GameID = Column(Integer, ForeignKey('Game.id'), nullable=False)

    @classmethod
    def create_board(cls, game, owner):
        board = Board()

        board.PlayerName = owner
        board.GameID = game

        board = Database.insert(board)

        return board

