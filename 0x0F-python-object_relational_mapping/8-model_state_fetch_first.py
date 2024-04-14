#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
If the table states is empty, print Nothing followed by a new line.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    f_state = session.query(State).order_by(State.id).first()
    if (f_state):
        print("{}: {}".format(f_state.id, f_state.name))
    else:
        print("Nothing")
