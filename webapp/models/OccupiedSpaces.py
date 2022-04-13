from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, and_
from database.base import Base
import re

from database.database_object import Database
from models.BaseModel import BaseModel
from models.Board import Board


class OccupiedSpaces(Base, BaseModel):
    __tablename__ = "OccupiedSpaces"

    BoardID = Column(Integer, ForeignKey('Board.id'), nullable=False)
    ShipID = Column(String, nullable=False)
    Position = Column(String, nullable=False)
    isHit = Column(Boolean, default=False)

    @classmethod
    def get_by_board(cls, board_to_be_got):
        entry = None
        with Database.get_session() as session:
            entry = session.query(cls).filter(cls.BoardID == board_to_be_got).all()

        return entry

    @classmethod
    def occupy_space(cls, board: Board, ship: int, pos: str):
        occupation = OccupiedSpaces()
        occupation.BoardID = board.id
        occupation.ShipID = ship
        occupation.Position = pos
        occupation = Database.insert(occupation)
        return occupation

    @classmethod
    def check_validity(cls, move_str, board):
        res = re.search("([A-Ja-j])(10|[1-9])$", move_str);

        if not res:
            raise InvalidSpaceException

        y = res.group(1)
        x = res.group(2)

        occupied_spaces = OccupiedSpaces.get_by_board(board.id)
        occupied_positions = list()
        for space in occupied_spaces:
            occupied_positions.append(space.Position)
        if move_str in occupied_positions:
            raise SpaceAlreadyOccupiedException()

        occupied_spaces = OccupiedSpaces.get_by_board(board.id)

        surrounding = list()
        surrounding.append(str(chr(ord(y)-1)) + str(int(x)-1))
        surrounding.append(str(chr(ord(y)-1)) + str(int(x)))
        surrounding.append(str(chr(ord(y)-1)) + str(int(x)+1))
        surrounding.append(str(chr(ord(y))) + str(int(x)-1))
        surrounding.append(str(chr(ord(y))) + str(int(x)+1))
        surrounding.append(str(chr(ord(y)+1)) + str(int(x)-1))
        surrounding.append(str(chr(ord(y)+1)) + str(int(x)))
        surrounding.append(str(chr(ord(y)+1)) + str(int(x)+1))
        for space in occupied_spaces:
            if space.Position in surrounding:
                raise SpaceAlreadyOccupiedException()

        return res


class SpaceAlreadyOccupiedException(Exception):
    pass


class InvalidSpaceException(Exception):
    pass
