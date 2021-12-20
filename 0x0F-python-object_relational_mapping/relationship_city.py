#!/usr/bin/python3
""" relationship city """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """ class city """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement='auto',
        nullable=False,
        unique=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
