#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from the database
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
    deletes = ses.query(State).order_by(State.id).all()
    for row in deletes:
        if 'a' in row.name:
            ses.delete(row)
    ses.commit()
    ses.close()
