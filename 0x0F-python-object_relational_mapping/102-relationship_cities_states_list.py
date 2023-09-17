#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password,
                                                         db_name),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects with linked State objects
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
