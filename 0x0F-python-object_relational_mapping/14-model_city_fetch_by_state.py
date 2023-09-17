#!/usr/bin/python3
"""
Fetches and prints all City objects from the hbtn_0e_14_usa database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and bind session
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password,
                                                         db_name),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and print them
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State).get(city.state_id).name
        print("{}: ({}) {}".format(state_name, city.id, city.name))
