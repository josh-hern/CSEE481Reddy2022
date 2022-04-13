from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from database.base import Base

import os


class Database:
    engine = None

    @classmethod
    def create_tables(cls):
        from models.BaseModel import BaseModel
        from models.OccupiedSpaces import OccupiedSpaces
        from models.AttackMoves import AttackMoves
        from models.Game import Game
        from models.Ship import Ship
        from models.Board import Board

        Base.metadata.create_all(bind=cls.engine)

    @classmethod
    def insert(cls, entry):
        if not cls.engine:
            cls.create_engine(os.path.dirname(__file__), "battleship_database.db")
        posted_entry = None
        with Session(cls.engine) as session:
            session.add(entry)
            session.commit()
            session.refresh(entry)
            posted_entry = entry
        return posted_entry

    @classmethod
    def get_session(cls):
        if not cls.engine:
            cls.create_engine(os.path.dirname(__file__), "battleship_database.db")
        return Session(cls.engine)

    @classmethod
    def create_engine(cls, dir_name, filename):
        cls.engine = create_engine('sqlite:///' + dir_name + '/' + filename)


if __name__ == "__main__":
    Database.create_engine(os.path.dirname(__file__), "battleship_database.db")
    Database.create_tables()
    # from database_query_insert import GeneralInitialization

    # GeneralInitialization()
