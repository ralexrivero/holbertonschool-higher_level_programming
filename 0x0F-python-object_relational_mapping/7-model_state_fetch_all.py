#!/usr/bin/python3
"""
Script that lists all State objects from the database
"""


if __name__ == "__main__":
    from sys import argv

    from model_state import Base, State

    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
