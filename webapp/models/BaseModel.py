import datetime
from datetime import datetime

from sqlalchemy import ForeignKey, Column, Integer, DATETIME, Boolean

from database.database_object import Database


class BaseModel:
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DATETIME(timezone=True), default=lambda: datetime.now())
    updated_at = Column(DATETIME(timezone=True), nullable=True)

    @classmethod
    def get_all(cls):
        rows = list()
        with Database.get_session() as session:
            rows = session.query(cls).all()
        return rows

    @classmethod
    def get_by_id(cls, id_to_be_got):
        entry = None
        with Database.get_session() as session:
            entry = session.query(cls).filter(cls.id == id_to_be_got).first()

        return entry

    @classmethod
    def update(cls, entry_id, pair):
        posted_entry = None
        if 'id' not in pair.keys() and 'created_at' not in pair.keys():
            with Database.get_session() as session:
                session.query(cls).filter(cls.id==entry_id).update(pair)
                session.query(cls).filter(cls.id==entry_id).update({'updated_at': datetime.now()})
                session.commit()
            return cls.get_by_id(entry_id)

        else:
            raise InvalidUpdateException()

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class InvalidUpdateException(BaseException):
    pass


class WhatTheFuckException(BaseException):
    pass
