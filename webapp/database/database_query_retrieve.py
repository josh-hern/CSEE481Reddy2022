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
    print(result)
    if result:
        return True
    else:
        return False


print(get_space('///battleship_database.db', 'a4'))
