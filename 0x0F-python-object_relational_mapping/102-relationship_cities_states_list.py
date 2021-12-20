#!/usr/bin/python3
""" script that lists all City objects """

from sys import argv
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    name_db = argv[3]

    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, name_db),
        pool_pre_ping=True
    )
    Base.metadata.create_all(eng)
    s = sessionmaker(bind=eng)
    ses = s()

    cts = ses.query(City).order_by(City.id).all()

    for ct in cts:
        print('{}: {} -> {}'.format(ct.id, ct.name, ct.state.name))
