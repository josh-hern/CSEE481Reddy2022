import os
from construct_database import create_tables

os.remove('../database/battleship_database.db')
create_tables()
