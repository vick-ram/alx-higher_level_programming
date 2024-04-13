#!/usr/bin/python3
"""Start link class to table in database"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class State(Base):
    """Class representing the states table"""
    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True,
        nullable=False, autoincrement=True
    )
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", back_populates="state", cascade="all, delete-orphan"
    )
