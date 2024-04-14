#!/usr/bin/python3
"""our model to be imported
"""

from sqlalchemy import (
    create_engine,
    inspect,
    Column,
    String,
    Integer)

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()



class State(Base):
    __tablename__ = 'states'
    id   = Column(Integer, primary_key=True)
    name = Column(String(128))
