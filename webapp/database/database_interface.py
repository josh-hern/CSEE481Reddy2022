"""
This file will be for operations involving the database
"""
import database.construct_database as database
from database.database_query_retrieve import *
from sqlalchemy.orm import sessionmaker


class GameConnector:
    """
    This class will handle game connections, and their usage with the database
    """

    def __init__(self, database_location='///battleship_database.db'):
        self.database_location_sqlalchemy = database_location
        print(self.database_location_sqlalchemy)
        engine = create_engine(f'sqlite:{self.database_location_sqlalchemy}')
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
        attack_adder.PlayerID = json_decoded['player']
        attack_adder.Position = json_decoded['attack_space']
        is_hit = self.check_space(json_decoded['attack_space'])
        if is_hit:
            self.add_hit(player=json_decoded['player'], position=json_decoded['attack_space'])
            attack_adder.isHit = 1
            session.add(attack_adder)
            session.commit()
            session.close()
            print("hit!")
            if self.check_ship_sunk(json_decoded['attack_space']):
                ship_id = {1: 'carrier',
                           2: 'battleship',
                           3: 'destroyer',
                           4: 'submarine',
                           5: 'patrol boat'}
                database_row = get_entire_row(self.database_location_sqlalchemy, json_decoded['attack_space'])
                # print(database_row, 'database_row')
                ship_num = database_row[1]
                print(f'you sunk my {ship_id[ship_num]}!')
        else:
            attack_adder.isHit = 0
            session.add(attack_adder)
            session.commit()
            session.close()
            print("miss!")

    def check_space(self, space):
        """
        Checks if a space has a ship in it

        :return:
        :rtype:
        """
        is_space_occupied = get_space(self.database_location_sqlalchemy, space)
        return is_space_occupied

    def add_ship_position(self, json_input):
        """
        Adds ship positions from game startup
        Needs to know which ship and the space location

        :return:
        :rtype:
        """
        # {ship_space: <space_string>, ship_direction: <ship_direction>, ship_type: <ship_ID>, player: <int_ID>}
        json_decoded = self._decode_json(json_input)
        ship_id_to_length = {'Patrol Boat': 2,
                             'Submarine': 3,
                             'Destroyer': 3,
                             'Battleship': 4,
                             'Carrier': 5
                             }
        ship_length = ship_id_to_length[str(json_decoded['ship_type'])]
        session = self.sessionmaker_session()
        ship_adder = database.OccupiedSpacesTable()
        ship_adder.PlayerID = json_decoded['player']
        ship_adder.ShipID = json_decoded['ship_type']
        initial_space = json_decoded['ship_space']
        ship_adder.Position = initial_space
        ship_adder.isHit = 0
        session.add(ship_adder)
        session.commit()
        session.close()
        # if json_decoded['ship_direction'] == 'v':
        #     initial_row = str(initial_space[0])
        #     for i in range(1, ship_length):
        #         session = self.sessionmaker_session()
        #         ship_adder = database.OccupiedSpacesTable()
        #         ship_adder.PlayerID = json_decoded['player']
        #         ship_adder.ShipID = json_decoded['ship_type']
        #         position_string = f'{chr(ord(initial_row) + i)}{initial_space[1]}'
        #         ship_adder.Position = position_string
        #         ship_adder.isHit = 0
        #         session.add(ship_adder)
        #         session.commit()
        #         session.close()
        # else:
        #     initial_number = int(initial_space[1])
        #     for i in range(1, ship_length):
        #         session = self.sessionmaker_session()
        #         ship_adder = database.OccupiedSpacesTable()
        #         ship_adder.PlayerID = json_decoded['player']
        #         ship_adder.ShipID = json_decoded['ship_type']
        #         position_string = f'{initial_space[0]}{initial_number + i}'
        #         ship_adder.Position = position_string
        #         ship_adder.isHit = 0
        #         session.add(ship_adder)
        #         session.commit()
        #         session.close()

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
            if entry[0] == 1:
                continue
            else:
                return False
        return True

    def add_hit(self, player, position):
        engine = create_engine(f'sqlite:{self.database_location_sqlalchemy}', echo=True)
        database_row = get_entire_row(self.database_location_sqlalchemy, position)
        # print(database_row, 'database_row')
        ship_id = database_row[1]
        print(ship_id, player, position)
        connection = engine.connect()
        query = f'UPDATE OccupiedSpaces SET isHit = True WHERE (ShipID = {ship_id} AND PlayerID = {player} AND Position LIKE \"{position}\");'
        connection.execute(query)

    @staticmethod
    def _decode_json(input_json):
        """
        Decodes json to a python dictionary

        :return:
        :rtype:
        """
        import json
        # print(input_json)
        space = input_json.find('.json')
        # print(space)
        if input_json.find('.json') > 0:
            with open(input_json, 'r') as json_file:
                json_to_dict = json.load(json_file)
        else:
            json_to_dict = json.loads(input_json)
        return json_to_dict

# test = GameConnector()
# # print(test.check_ship_sunk('a4'))
# test.add_ship_position('{"ship_space": "a6", "ship_direction": "v", "ship_type": "Destroyer", "player": 1}')
# test.add_ship_position('{"ship_space": "b4", "ship_direction": "h", "ship_type": "Carrier", "player": 2}')
# test.add_ship_position('{"ship_space": "c2", "ship_direction": "v", "ship_type": "Battleship", "player": 2}')
# test.add_attack_to_database('{"attack_space": "a5", "player": 1}')
# test.add_attack_to_database('{"attack_space": "a6", "player": 1}')
# test.add_attack_to_database('{"attack_space": "a7", "player": 1}')
