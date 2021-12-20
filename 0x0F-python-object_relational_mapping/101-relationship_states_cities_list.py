#!/usr/bin/python3
""" script that lists all State objects """

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
    sts = ses.query(State).order_by(State.id).all()
    for st in sts:
        print('{}: {}'.format(st.id, st.name))
        for ct in st.cities:
            print('	{}: {}'.format(ct.id, ct.name))
