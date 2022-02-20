"""
This file will be for operations involving the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import infrastructure.database as database


class GameConnector:
    """
    This class will handle game connections, and their usage with the database
    """

    def __init__(self, database_location='///../database/battleship_database.db'):
        self.database_location_sqlalchemy = database_location
        engine = create_engine(f'sqlite:{self.database_location_sqlalchemy}', echo=True)
        self.sessionmaker_session = sessionmaker(bind=engine)

    def add_attack_to_database(self, json_input):
        """
        Adds an input attack to database

        :return:
        :rtype:
        """
        # {attack_space: <space_string>, player: <int_ID>}
        json_decoded = self._decode_json(json_input)

        '''
        Steps:
        1. Add attack to table for proper player
        2. cross reference occupied_spaces table to see if the space is used
        3a. If so, check if other adjacent spaces have also been attacked
        3a2. If all adjacent spaces have also been attacked, record ship as sunk
        3a3. else, just add the hit
        3b If space is not used, add a miss
        '''

        session = self.sessionmaker_session()
        attack_adder = database.AttackMovesTable()
        attack_adder.ID = json_decoded['player']
        attack_adder.Position = json_decoded['attack_space']

        pass

    def check_space(self):
        """
        Checks if a space has already been attacked

        :return:
        :rtype:
        """
        pass

    def add_ship_position(self):
        """
        Adds ship positions from game startup

        :return:
        :rtype:
        """
        pass

    @staticmethod
    def _decode_json(input_json):
        """
        Decodes json to a python dictionary

        :return:
        :rtype:
        """
        import json
        if input_json.find('.json'):
            with open(input_json, 'r') as json_file:
                json_to_dict = json.load(json_file)
        else:
            json_to_dict = json.loads(input_json)
        return json_to_dict


class ESPConnector:
    """
    This class will handle ESP connections, and their usage with the database
    """

    def __init__(self):
        pass

    def add_attack_to_database(self):
        """
        Adds an input attack to database

        :return:
        :rtype:
        """
        pass

    def check_space(self):
        """
        Checks if a space has already been attacked

        :return:
        :rtype:
        """
        pass
