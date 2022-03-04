"""
This file will be for operations involving the database
"""
from sqlalchemy.orm import sessionmaker

import construct_database as database
from database_query_retrieve import *


class GameConnector:
    """
    This class will handle game connections, and their usage with the database
    """

    def __init__(self, database_location='///battleship_database.db'):
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

        attack_adder = database.AttackMovesTable()
        attack_adder.ID = json_decoded['player']
        attack_adder.Position = json_decoded['attack_space']
        is_hit = self.check_space(json_decoded['attack_space'])
        if self.check_ship_sunk(json_decoded['attack_space']):
            # Add attack move to table
            print('you sunk {ship}!')
        elif is_hit:
            # Add attack move to table
            print("hit!")
        else:
            print("miss!")

    def check_space(self, space):
        """
        Checks if a space has a ship in it

        :return:
        :rtype:
        """
        is_space_occupied = get_space(self.database_location_sqlalchemy, space)
        return is_space_occupied

    def add_ship_position(self):
        """
        Adds ship positions from game startup

        :return:
        :rtype:
        """
        pass

    def check_ship_sunk(self, space):
        """
        given a position, check if the ship at that position is sunk

        :return:
        :rtype:
        """
        database_row = get_entire_row(self.database_location_sqlalchemy, space)
        # print(database_row, 'database_row')
        ship_id = database_row[1]
        list_of_hits = get_similar_ship_id(self.database_location_sqlalchemy, ship_id)
        # print(list_of_hits)
        for entry in list_of_hits:
            # print(entry[0], 'entry')
            if entry[0] == 'True':
                continue
            else:
                return False
        return True

    @staticmethod
    def decode_json(input_json):
        """
        Decodes json to a python dictionary

        :return:
        :rtype:
        """
        import json
        print(input_json)
        space = input_json.find('.json')
        print(space)
        if input_json.find('.json') > 0:
            with open(input_json, 'r') as json_file:
                json_to_dict = json.load(json_file)
        else:
            json_to_dict = json.loads(input_json)
        return json_to_dict
