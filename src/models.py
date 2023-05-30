import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    suscription_date = Column(String(250), nullable=False)
    email = Column(Integer, nullable=False)
    suscription_date = Column(String(250), nullable=False)
  

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    total_favourite_characters = Column(Integer, ForeignKey('favourites_characters.id')) 
    total_favourite_planetss = Column(Integer, ForeignKey('favourites_planets.id'))  

class Favourites_characters(Base):
    __tablename__ = 'favourites_characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_ID = Column(Integer, ForeignKey('characters.id'))
    user_ID = Column(Integer, ForeignKey('user.id'))
   

class Favourites_planets(Base):
    __tablename__ = 'favourites_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_ID = Column(Integer, ForeignKey('planets.id'))
    user_ID = Column(Integer, ForeignKey('user.id'))
   

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    character_lastname = Column(String(250))
     

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    population = Column(Integer)





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
