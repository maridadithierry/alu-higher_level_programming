#!/usr/bin/python3
<<<<<<< HEAD
""" prints the State object with the name passed as argument from the database
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
    instance = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
=======
""" lists all State objects that contain
the letter a from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    records = session.query(State).filter(State.name == "{}".format(
        sys.argv[4])).all()

    if records:
        for rec in records:
            if rec.name == sys.argv[4]:
                print("{}".format(rec.__dict__['id']))
    else:
        print("Not found")

    session.close()
>>>>>>> ca8a0c3d0449bd06a28081efb6904e29e2f97e70
