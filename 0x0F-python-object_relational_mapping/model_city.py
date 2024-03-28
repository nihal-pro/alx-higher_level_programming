#!/usr/bin/python3
'''Write a python file that contains the class definition'''

import sqlalchemy
from model_state import Base


class City(Base):
    """ Create class table """
    __tablename__ = "cities"
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    state_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.sql.schema.ForeignKey('states.id'),
        nullable=False)
