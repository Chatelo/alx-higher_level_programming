#!/usr/bin/python3
"""
Defines the class City
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """
    City class that inherits from Base
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
