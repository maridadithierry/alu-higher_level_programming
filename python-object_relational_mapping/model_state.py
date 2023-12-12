#!/usr/bin/python3
<<<<<<< HEAD
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
=======
'''
    Using the SQL Alchemy in defining a database
    states Database table
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    '''A class defination of a table in the sql'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
>>>>>>> ca8a0c3d0449bd06a28081efb6904e29e2f97e70
    name = Column(String(128), nullable=False)
