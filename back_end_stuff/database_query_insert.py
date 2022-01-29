"""
This file will be for handling database insertions (not initialization, but data after this occurs
"""
from construct_database import ShipDesignation
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker, relationship


def initialization():
    # trying to add rows to database table. Will work on more later
    engine = create_engine('sqlite:///../database/battleship_database.db', echo=True)
    session = sessionmaker(bind=engine)

    create_carrier(session)
    create_battleship(session)
    create_cruiser(session)
    create_destroyer(session)
    create_submarine(session)


def create_carrier(sessionmaker_session):
    session = sessionmaker_session()
    carrier = ShipDesignation()
    carrier.id = 1
    carrier.length = 5
    carrier.ship_name = "Carrier"
    session.add(carrier)
    session.commit()
    session.close()


def create_battleship(sessionmaker_session):
    session = sessionmaker_session()
    carrier = ShipDesignation()
    carrier.id = 2
    carrier.length = 4
    carrier.ship_name = "Battleship"
    session.add(carrier)
    session.commit()
    session.close()


def create_cruiser(sessionmaker_session):
    session = sessionmaker_session()
    carrier = ShipDesignation()
    carrier.id = 3
    carrier.length = 3
    carrier.ship_name = "Cruiser"
    session.add(carrier)
    session.commit()
    session.close()


def create_submarine(sessionmaker_session):
    session = sessionmaker_session()
    carrier = ShipDesignation()
    carrier.id = 4
    carrier.length = 3
    carrier.ship_name = "Submarine"
    session.add(carrier)
    session.commit()
    session.close()


def create_destroyer(sessionmaker_session):
    session = sessionmaker_session()
    carrier = ShipDesignation()
    carrier.id = 5
    carrier.length = 2
    carrier.ship_name = "Destroyer"
    session.add(carrier)
    session.commit()
    session.close()