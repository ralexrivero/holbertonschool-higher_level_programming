#!/usr/bin/python3
"""create a state and a city"""

from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    name_db = argv[3]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(username, password, name_db),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    s = sessionmaker(bind=eng)
    ses = s()
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    ses.add(new_city)
    ses.commit()
    ses.close()
