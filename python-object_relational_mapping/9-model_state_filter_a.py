#!/usr/bin/python3
<<<<<<< HEAD
""" prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")
=======
"""A script that lists all records with letter a"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                    )
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    states = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
>>>>>>> ca8a0c3d0449bd06a28081efb6904e29e2f97e70
