#!/usr/bin/python3
"""Create the State "California" with the City "San Francisco"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database)
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    califonia = State(name="Califonia", cities=[City(name="San Francisco")])
    session.add(califonia)
    session.commit()
    session.close()
