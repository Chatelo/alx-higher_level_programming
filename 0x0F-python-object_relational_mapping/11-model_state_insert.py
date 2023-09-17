#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password,
                                                         db_name),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the ID of the newly created state
    print(new_state.id)
