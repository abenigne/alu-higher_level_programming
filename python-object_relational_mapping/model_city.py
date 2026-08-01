#!/usr/bin/python3
"""This module defines the City class, mapped to the MySQL table
cities, using SQLAlchemy's declarative base.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import Base


class City(Base):
    """Represents a city, linked to the MySQL table cities."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", backref="cities")
