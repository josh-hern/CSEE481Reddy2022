"""
This file will be for handling database retrieval
"""

from sqlalchemy import create_engine


def get_occupied_spaces(database_location, space):
    engine = create_engine(f'sqlite:{database_location}', echo=True)
    connection = engine.connect()
    table_name = "OccupiedSpaces"
    query = f'SELECT Position FROM {table_name} WHERE (Position LIKE \"{space}\");'
    result = connection.execute(query)
    print(list(result))
    # sessionmaker_session = sessionmaker(bind=engine)()
    # occupied_spaces = database.OccupiedSpacesTable()
    # # print(occupied_spaces.__table__.columns)
    # q = sessionmaker_session.query(occupied_spaces.__table__).filter(occupied_spaces.Position == space)
    # return q


print(get_occupied_spaces('///battleship_database.db', 'a4'))
