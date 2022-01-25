from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DATETIME, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()


class ShipDesignation(Base):
    """
    Creates the ShipDesignation table
    """
    __tablename__ = "ShipDesignation"

    ship_id = Column('ship_id', Integer, primary_key=True)
    length = Column('length', Integer)
    ship_name = Column('ship_name', String)


class ShipPlacement(Base):
    """
    Creates the ShipPlacement table
    """
    __tablename__ = "ShipPlacement"

    id = Column('id', Integer, primary_key=True)
    player = Column('player', Integer)
    ship_id = Column('ship_id', Integer, ForeignKey(ShipDesignation.ship_id))


class AttackTable(Base):
    """
    Creates the attacktable
    """
    __tablename__ = "AttackTable"

    time_stamp = Column('time_stamp', DATETIME, primary_key=True)
    player = Column('player', Integer)
    space_attacked = Column('space_attacked', String)
    hit = Column('hit', Boolean)


engine = create_engine('sqlite:///../database/battleship_database.db', echo=True)
Base.metadata.create_all(bind=engine)



