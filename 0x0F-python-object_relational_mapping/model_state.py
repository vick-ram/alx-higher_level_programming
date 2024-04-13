#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from base import Base


class State(Base):
    """Class representing the states table"""
    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True,
        nullable=False, autoincrement=True
    )
    name = Column(String(128), nullable=False)
