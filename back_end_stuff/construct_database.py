from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()


class ShipPlacement(Base):
    __tablename__ = "ShipPlacement"

    ship_id = Column('ship_id', Integer, primary_key=True)
    length = Column('length', Integer)
    ship_name = Column('ship_name', String)



engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)



