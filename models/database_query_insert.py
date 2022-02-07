"""
This file will be for handling database insertions (not initialization, but data after this occurs
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.construct_database import ShipTable, PlayerTable


class InitializationOfShips:
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
        carrier = ShipTable()
        carrier.id = 1
        carrier.isSunk = False
        session.add(carrier)
        session.commit()
        session.close()

    def create_battleship(self):
        session = self.sessionmaker_session()
        battleship = ShipTable()
        battleship.id = 2
        battleship.isSunk = False
        session.add(battleship)
        session.commit()
        session.close()

    def create_cruiser(self):
        session = self.sessionmaker_session()
        cruiser = ShipTable()
        cruiser.id = 3
        cruiser.isSunk = False
        session.add(cruiser)
        session.commit()
        session.close()

    def create_submarine(self):
        session = self.sessionmaker_session()
        submarine = ShipTable()
        submarine.id = 4
        submarine.isSunk = False
        session.add(submarine)
        session.commit()
        session.close()

    def create_destroyer(self):
        session = self.sessionmaker_session()
        destroyer = ShipTable()
        destroyer.id = 5
        destroyer.isSunk = False
        session.add(destroyer)
        session.commit()
        session.close()


class InitializationOfPlayers:
    def __init__(self):
        engine = create_engine('sqlite:///../database/battleship_database.db', echo=True)
        self.sessionmaker_session = sessionmaker(bind=engine)

        self.ready_player_one()
        self.ready_player_two()

    def ready_player_one(self):
        session = self.sessionmaker_session()
        player1 = PlayerTable()
        player1.ID = 1
        session.add(player1)
        session.commit()
        session.close()

    def ready_player_two(self):
        session = self.sessionmaker_session()
        player2 = PlayerTable()
        player2.ID = 2
        session.add(player2)
        session.commit()
        session.close()


class InitializationOfOccupiedSpaces:
    """
    Not sure if we will need this class. It depends on if we want to prefill the database with possible occupied
    spaces or not
    """
    pass
