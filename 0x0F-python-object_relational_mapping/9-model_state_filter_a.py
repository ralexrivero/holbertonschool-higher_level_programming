#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
"""
from sys import argv
from model_state import Base, State
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
    for state in ses.query(State).order_by(State.id.asc()).all():
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
    ses.close()
