"""
This file will be for handling database insertions (not initialization, but data after this occurs
"""
from construct_database import ShipDesignation
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker, relationship


def initialization():
    # trying to add rows to database table. Will work on more later
    engine = create_engine('sqlite://../database/battleship_database.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    carrier = ShipDesignation()
    carrier.id = 1
    carrier.length = 5
    carrier.ship_name = "Carrier"
    session.add(carrier)
    session.commit()

    session.close()
