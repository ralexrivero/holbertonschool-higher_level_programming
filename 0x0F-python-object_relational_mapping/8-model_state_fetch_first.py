#!/usr/bin/python3
"""
prints the first State object from the database
"""
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    state = sess.query(State).first()

    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    sess.close()
