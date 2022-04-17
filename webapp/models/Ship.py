from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, DATETIME, Boolean
from database.base import Base
from database.database_object import Database
from models.BaseModel import BaseModel
from models.OccupiedSpaces import OccupiedSpaces


class Ship(Base, BaseModel):
    __tablename__ = "Ship"

    ShipName = Column('ShipName', String)
    BoardID = Column(Integer, ForeignKey('Board.id'))
    isSunk = Column('isSunk', Boolean, default=False)
    length = Column(Integer)

    @classmethod
    def add_ship(cls, game, ship_type, board, position, rotated: bool = False):
        ship = Ship()

        ship.ShipName = ship_type

        ship.BoardID = board.id
        ship.length = Ship.get_length(ship_type)
        positions = Ship.check_placement(board, position, rotated, ship.length)

        current_ships = Ship.get_by_board(board.id)
        current_ship_names = list()

        for current_ship in current_ships:
            current_ship_names.append(current_ship.ShipName)
        if ship_type in current_ship_names:
            raise ShipAlreadyPlacedException()

        ship = Database.insert(ship)

        for pos in positions:
            OccupiedSpaces.occupy_space(board, ship.id, pos)

        return ship

    @classmethod
    def check_placement(cls, board, position, rotated: bool, length):
        positions = list()

        for i in range(length):
            res = OccupiedSpaces.check_validity(position, board)
            positions.append(position)
            if not rotated:
                position = res.group(1) + str(int(res.group(2)) + 1)
            else:
                position = str(chr(ord(res.group(1)) + 1)) + str(res.group(2))

        return positions

    @classmethod
    def get_length(cls, name):
        length = None
        if name.lower() == "carrier":
            length = 5
        elif name.lower() == "battleship":
            length = 4
        elif name.lower() == "destroyer":
            length = 3
        elif name.lower() == "submarine":
            length = 3
        elif name.lower() == "patrol boat":
            length = 2
        else:
            raise InvalidShipNameException()

        return length

    @classmethod
    def get_by_board(cls, board_to_be_got):
        entry = None
        with Database.get_session() as session:
            entry = session.query(cls).filter(cls.BoardID == board_to_be_got).all()

        return entry

    def check_if_sunk(self):
        spaces = OccupiedSpaces.get_by_ship(self.id)
        sunk = True
        for space in spaces:
            if not space.isHit:
                sunk = False

        if sunk:
            Ship.update(self.id, {"isSunk": True})
            space_pos = list()
            for space in spaces:
                OccupiedSpaces.update(space.id, {"isSunk": True})

        return sunk


class InvalidShipNameException(Exception):
    pass


class ShipAlreadyPlacedException(Exception):
    pass
