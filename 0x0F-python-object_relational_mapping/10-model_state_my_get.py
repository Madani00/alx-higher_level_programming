#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
If no state has the name you searched for, display Not found.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    f_state = session.query(State).filter(State.name == (argv[4],)).first()
    if (f_state):
        print("{}".format(f_state.id))
    else:
        print("Not found")
