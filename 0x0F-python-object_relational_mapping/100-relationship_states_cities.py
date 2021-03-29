#!/usr/bin/python3
"""Start link class to table in database """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_id = len(session.query(State).all()) + 1
    cali = State(name="California", id=new_id)
    session.add(cali)
    session.commit()
    sanfran = City(name="San Francisco", state_id=new_id)
    session.add(sanfran)
    session.commit()
    session.close()
