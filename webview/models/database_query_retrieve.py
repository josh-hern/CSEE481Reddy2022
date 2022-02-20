"""
This file will be for handling database retrieval
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import infrastructure.database as database


def get_occupied_spaces(database_location, space):
    engine = create_engine(f'sqlite:{database_location}', echo=True)
    sessionmaker_session = sessionmaker(bind=engine)()
    occupied_spaces = database.OccupiedSpacesTable()
    sessionmaker_session.query(occupied_spaces.Position).filter(occupied_spaces.Position.like(space))
    pass
