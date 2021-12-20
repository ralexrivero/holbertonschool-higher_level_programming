#!/usr/bin/python3
"""
changes the name of a State object from the database
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
    new_state = ses.query(State).filter_by(id=2).first()
    new_state.name = 'New Mexico'
    ses.add(new_state)
    ses.commit()
    ses.close()
