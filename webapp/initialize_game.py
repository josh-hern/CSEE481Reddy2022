import os

from webapp.database import database_interface

battleship_game = None


def initialize_game():
    global battleship_game
    absolute_path = os.path.abspath(__file__)
    battleship_game = database_interface.GameConnector(f'///database/battleship_database.db')
