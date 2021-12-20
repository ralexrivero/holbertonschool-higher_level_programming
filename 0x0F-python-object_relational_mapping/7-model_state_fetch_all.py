#!/usr/bin/python3
"""
Script that lists all State objects from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ don't execute on import """
    user = argv[1]
    password = argv[2]
    database = argv[3]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    states = sess.query(State).order_by(State.id.asc()).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    sess.close()
