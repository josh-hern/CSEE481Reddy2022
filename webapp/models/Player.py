from sqlalchemy import Column, Integer
from database.base import Base
from database.database_object import Database
from models.BaseModel import BaseModel


class Player(Base, BaseModel):
    __tablename__ = "Player"

    @classmethod
    def create_default_players(cls):
        player1 = Player()
        player1.id = 1
        Database.insert(player1)

        player2 = Player()
        player2.id = 2
        Database.insert(player2)

