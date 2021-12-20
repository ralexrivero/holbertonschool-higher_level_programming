#!/usr/bin/python3
"""
lists all City objects from the database
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    ses = Session(eng)
    new_table = ses.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id.asc()).all()
    for cities, states in new_table:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    ses.close()
