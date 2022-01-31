"""
This file will be for handling database insertions (not initialization, but data after this occurs
"""
from construct_database import ShipDesignation
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker, relationship


class Initialization:
    def __init__(self):
        engine = create_engine('sqlite:///../database/battleship_database.db', echo=True)
        self.sessionmaker_session = sessionmaker(bind=engine)

        self.create_carrier()
        self.create_battleship()
        self.create_cruiser()
        self.create_destroyer()
        self.create_submarine()

    def create_carrier(self):
        session = self.sessionmaker_session()
        carrier = ShipDesignation()
        carrier.id = 1
        carrier.length = 5
        carrier.ship_name = "Carrier"
        session.add(carrier)
        session.commit()
        session.close()

    def create_battleship(self):
        session = self.sessionmaker_session()
        carrier = ShipDesignation()
        carrier.id = 2
        carrier.length = 4
        carrier.ship_name = "Battleship"
        session.add(carrier)
        session.commit()
        session.close()

    def create_cruiser(self):
        session = self.sessionmaker_session()
        carrier = ShipDesignation()
        carrier.id = 3
        carrier.length = 3
        carrier.ship_name = "Cruiser"
        session.add(carrier)
        session.commit()
        session.close()

    def create_submarine(self):
        session = self.sessionmaker_session()
        carrier = ShipDesignation()
        carrier.id = 4
        carrier.length = 3
        carrier.ship_name = "Submarine"
        session.add(carrier)
        session.commit()
        session.close()

    def create_destroyer(self):
        session = self.sessionmaker_session()
        carrier = ShipDesignation()
        carrier.id = 5
        carrier.length = 2
        carrier.ship_name = "Destroyer"
        session.add(carrier)
        session.commit()
        session.close()