from sqlalchemy import create_engine, Column, Integer, String, DATETIME, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class GameTable(Base):
    __tablename__ = "Game"

    ID = Column('ID', Integer, primary_key=True)
    Start = Column('Start', DATETIME)


class PlayerTable(Base):
    __tablename__ = "Player"

    ID = Column('ID', Integer, primary_key=True)


class ShipTable(Base):
    __tablename__ = "Ship"

    ID = Column('ID', Integer, primary_key=True)
    isSunk = Column('isSunk', Boolean)


class AttackMovesTable(Base):
    __tablename__ = "AttackMoves"

    ID = Column('ID', Integer, primary_key=True)
    Position = Column('Position', String)
    isHit = Column('isHit', Boolean)


class OccupiedSpacesTable(Base):
    __tablename__ = "OccupiedSpaces"

    PlayerID = Column('PlayerID', Integer)  # NOTE: remove primary key
    ShipID = Column('ShipID', Integer)
    Position = Column('Position', String)
    isHit = Column('isHit', Boolean)
    __mapper_args__ = {
        "primary_key": [PlayerID, ShipID, Position, isHit]
    }


def create_tables():
    engine = create_engine('sqlite:///battleship_database.db')
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()

    from database_query_insert import GeneralInitialization

    GeneralInitialization()
