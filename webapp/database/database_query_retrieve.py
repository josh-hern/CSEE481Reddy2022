"""
This file will be for handling database retrieval
"""

from sqlalchemy import create_engine


def get_space(database_location, space):
    engine = create_engine(f'sqlite:{database_location}', echo=True)
    connection = engine.connect()
    table_name = "OccupiedSpaces"
    query = f'SELECT Position FROM {table_name} WHERE (Position LIKE \"{space}\");'
    result = list(connection.execute(query))
    # print(result)
    if result:
        return True
    else:
        return False


def get_entire_row(database_location, space):
    engine = create_engine(f'sqlite:{database_location}', echo=True)
    connection = engine.connect()
    table_name = "OccupiedSpaces"
    query = f'SELECT * FROM {table_name} WHERE (Position LIKE \"{space}\");'
    result = list(connection.execute(query))
    if result:
        result = result[0]
    print(result)
    return result


def get_similar_ship_id(database_location, ship_id):
    engine = create_engine(f'sqlite:{database_location}', echo=True)
    connection = engine.connect()
    table_name = "OccupiedSpaces"
    query = f'SELECT isHit FROM {table_name} WHERE (ShipID LIKE \"{ship_id}\");'
    result = list(connection.execute(query))
    # for entry in result:
    #     print(entry[0])
    return result

# print(get_similar_ship_id('///battleship_database.db', 2))
