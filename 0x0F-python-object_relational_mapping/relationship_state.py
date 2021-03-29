#!/usr/bin/python3
"""State Relationship Class"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """State SQLAlchemy class"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    city = relationship("City", cascade="all, delete", backref="state")
