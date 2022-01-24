"""
This file will be for operations involving the database
"""
from os.path import exists


class GameConnector:
    """
    This class will handle game connections
    """
    def __init__(self):
        pass


class ESPConnector:
    """
    This class will handle ESP connections
    """
    def __init__(self):
        pass


class DatabaseInitialization:
    """
    This class will initialize the database or make sure it is initialized
    """
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def construct_database(self):
        """
        In this method the database file will be made and the tables defined
        :return:
        :rtype:
        """
        pass

    def check_if_constructed(self):
        """
        Checks if the database exists, and if not calls :meth:`construct_database`
        """
        if not self.database_exists():
            self.construct_database()
        else:
            print("database already exists!")

    @staticmethod
    def database_exists():
        """
        Simply checks if the database exists or not

        :return: Whether the database exists
        :rtype: bool
        """
        return exists("../database/battleship_database.db")


