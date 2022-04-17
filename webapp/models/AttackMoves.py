from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from database.base import Base
from database.database_object import Database
from models.BaseModel import BaseModel
from models.OccupiedSpaces import OccupiedSpaces
from models.Ship import Ship


class AttackMoves(Base, BaseModel):
    __tablename__ = "AttackMoves"

    BoardID = Column(Integer, ForeignKey('Board.id'))
    Position = Column(String, nullable=False)
    isAHit = Column(Boolean)
    isSunk = Column(Boolean, default=False)
    ShipID = Column(Integer, ForeignKey('Ship.id'), nullable=True)

    @classmethod
    def get_by_board(cls, board_to_be_got):
        entry = None
        with Database.get_session() as session:
            entry = session.query(cls).filter(cls.BoardID == board_to_be_got).all()

        return entry

    @classmethod
    def get_by_ship(cls, ship_to_be_got):
        entry = None
        with Database.get_session() as session:
            entry = session.query(cls).filter(cls.ShipID == ship_to_be_got).all()

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
        attack.isAHit = False
        for space in occupied_spaces:
            if space.Position == attack.Position:
                attack.isAHit = True
                attack.ShipID = space.ShipID
                OccupiedSpaces.update(space.id, {"isHit": True})

        Database.insert(attack)
        ship = None
        if attack.isAHit:
            ship = Ship.get_by_id(attack.ShipID)
            if ship.check_if_sunk():
                ship = Ship.get_by_id(attack.ShipID)
                attacks = AttackMoves.get_by_ship(ship.id)
                for attack_tmp in attacks:
                    attack = AttackMoves.update(attack_tmp.id, {"isSunk": True})

        return attack


class SpaceAlreadyAttackedException(BaseException):
    pass