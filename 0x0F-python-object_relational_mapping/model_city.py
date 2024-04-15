#!/usr/bin/python3
"""our model to be imported
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """class inherits from Base"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey=("states.id"), nullable=False)
    state = relationship("State", foreign_keys="City.state_id")
