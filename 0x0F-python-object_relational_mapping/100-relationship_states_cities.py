#!/usr/bin/python3
"""
Creates a State "California" with a City "San Francisco"
in the hbtn_0e_100_usa database.
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

    # Create a State "California" with City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)
    session.add(california)
    session.add(san_francisco)
    session.commit()
