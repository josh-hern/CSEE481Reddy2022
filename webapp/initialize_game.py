import os

from database import database_interface

battleship_game = None


def initialize_game():
    global battleship_game
    initial_dir = os.path.join(os.path.dirname(__file__), 'database', 'battleship_database.db')
    battleship_game = database_interface.GameConnector('///' + initial_dir.replace('\\', '/'))

    # battleship_game = database_interface.GameConnector(f'///database/battleship_database.db')
