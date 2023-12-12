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
    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'
    session.commit()
=======
"""script that changes the name of a State object
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    state = session.query(State).filter(State.id == 2).first()

    state.name = "New Mexico"

    session.commit()
    session.close()
>>>>>>> ca8a0c3d0449bd06a28081efb6904e29e2f97e70
