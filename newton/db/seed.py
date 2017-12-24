from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, Numeric, TIMESTAMP 

from newton.db.config import Base
import datetime
import os

class Trades(Base):
    __tablename__ = 'trades'
    time = Column('time', TIMESTAMP, primary_key=True)
    seq = Column('seq', Integer, primary_key=True)
    major = Column('major', String, primary_key=True)
    minor = Column('minor', String, primary_key=True)
    price = Column('price', Numeric, nullable=False)
    volume = Column('volume', Numeric, nullable=False)

