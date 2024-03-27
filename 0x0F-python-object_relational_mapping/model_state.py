#!/usr/bin/python3
'''Write a python file that contains the class definition'''

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Create class table """
    __tablename__ = "states"
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
