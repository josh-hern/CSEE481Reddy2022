from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, DATETIME, Boolean
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class GameTable(Base):
    __tablename__ = "Game"

    GameID = Column('GameID', Integer, primary_key=True)
    Start = Column('Start', DATETIME)
    End = Column('End', DATETIME, nullable=True)
    isSetup = Column('isSetup', Boolean, default=False)
    CurrentTurnPlayer = Column('CurrentTurnPlayer', Integer, ForeignKey('Player.PlayerID'))
    Winner = Column('Winner', Integer, ForeignKey('Player.PlayerID'))

class PlayerTable(Base):
    __tablename__ = "Player"

    PlayerID = Column('PlayerID', Integer, primary_key=True)


class ShipTable(Base):
    __tablename__ = "Ship"

    ShipID = Column('ShipID', Integer, primary_key=True)
    ShipName = Column('ShipName', String)
    PlayerID = Column('PlayerID', Integer, ForeignKey('Player.PlayerID'))
    GameID = Column('GameID', Integer, ForeignKey('Game.GameID'))
    isSunk = Column('isSunk', Boolean)


class AttackMovesTable(Base):
    __tablename__ = "AttackMoves"


    AttackID = Column('AttackID', Integer, primary_key=True)
    GameID = Column('GameID', Integer, ForeignKey('Game.GameID'))
    PlayerID = Column('PlayerID', Integer)
    Position = Column('Position', String)
    isHit = Column('isHit', Boolean)

class OccupiedSpacesTable(Base):
    __tablename__ = "OccupiedSpaces"

    OccupiedID = Column('OccupiedID', Integer, primary_key=True)
    PlayerID = Column('PlayerID', Integer)
    GameID = Column('GameID', Integer, ForeignKey('Game.GameID'))
    ShipID = Column('ShipID', String)
    Position = Column('Position', String)
    isHit = Column('isHit', Boolean)

# __ == dunder
# os.path.dirname(__file__)
def create_tables():
    engine = create_engine('sqlite:///'+ os.path.dirname(__file__) +'/battleship_database.db')
    Base.metadata.create_all(bind=engine)


if __name__ == "create_tables":
    create_tables()

    from database_query_insert import GeneralInitialization

    GeneralInitialization()
