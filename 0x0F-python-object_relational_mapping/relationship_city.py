#!/usr/bin/python3
"""
Contains the class definition of a City.
"""

from relationship_state import Base, State
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """
    City class, inherits from Base (from relationship_state)
    Represents a city with attributes: id, name, state_id
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
