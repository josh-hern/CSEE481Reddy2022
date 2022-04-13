from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from database.base import Base
from database.database_object import Database
from models.BaseModel import BaseModel
from models.OccupiedSpaces import OccupiedSpaces


class AttackMoves(Base, BaseModel):
    __tablename__ = "AttackMoves"

    BoardID = Column(Integer, ForeignKey('Board.id'))
    Position = Column(String, nullable=False)
    isAHit = Column('isHit', Boolean)

    @classmethod
    def get_by_board(cls, board_to_be_got):
        entry = None
        with Database.get_session() as session:
            entry = session.query(cls).filter(cls.BoardID == board_to_be_got).all()

        return entry

    @classmethod
    def attack(cls, board, position):
        attacks = AttackMoves.get_by_board(board.id)
        attack_positions = list()
        for attack in attacks:
            attack_positions.append(attack.Position)
        if position in attack_positions:
            raise SpaceAlreadyAttackedException()

        attack = AttackMoves()
        attack.BoardID = board.id
        attack.Position = position
        occupied_spaces = OccupiedSpaces.get_by_board(board.id)
        occupied_positions = list()
        for space in occupied_spaces:
            occupied_positions.append(space.Position)
        attack.isAHit = (position in occupied_positions)
        Database.insert(attack)

        return attack


class SpaceAlreadyAttackedException(BaseException):
    pass