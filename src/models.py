import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Date, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    birthYear = Column(Date, index=True, nullable=False)
    eyeColor = Column(String(250), nullable=False)
    films = Column(Integer, ForeignKey("films.id"), nullable=False)
    hairColor = Column(String(250), nullable=False)
    height = Column(Float, nullable=False) 
    homeWorld = Column(Integer, ForeignKey("planets.id"), nullable=False)
    mass = Column(Float, nullable=False) 
    name = Column(String(250), nullable=False) 
    skinColor = Column(String(250), nullable=False) 
    created = Column(DateTime, nullable=False) 
    edited = Column(DateTime, nullable=False) 
    specie = Column(Integer, ForeignKey("species.id"),  nullable=False)
    starship = Column(Integer, ForeignKey("starships.id"),  nullable=False) 
    url = Column(String(250), nullable=False) 
    vehicle = Column(Integer, ForeignKey("vehicles.id"),  nullable=False)

    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, index=True, nullable=False)
    diameter = Column(Integer, nullable=False)  
    edited = Column(DateTime, nullable=False) 
    films = Column(Integer, ForeignKey("films.id"), nullable=False) 
    gravity = Column(Integer, nullable=False) 
    name = Column(String(250), nullable=False) 
    orbital_period = Column(Integer, nullable=False) 
    population = Column(Integer, nullable=False) 
    residents = Column(String(250), nullable=False) 
    rotation_period = Column(Integer, nullable=False) 
    surface_water = Column(Integer, nullable=False) 
    terrain = Column(String(250), nullable=False) 
    url = Column(String(250), nullable=False) 

    def to_dict(self):
        return {}

class Specie(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)    
    average_height = Column(Integer, nullable=False)
    average_lifespan = Column(Integer, nullable=False)
    classification = Column(String(250), nullable=False)
    created = Column(DateTime, index=True, nullable=False)
    designation = Column(String(250), nullable=False)
    edited = Column(DateTime, nullable=False)
    eye_colors = Column(String(250), nullable=False)
    hair_colors = Column(String(250), nullable=False)
    homeworld = Column(Integer, ForeignKey("planets.id"), nullable=False)
    language = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    people = Column(String(250), nullable=False)
    films = Column(Integer, ForeignKey("films.id"), nullable=False)
    skin_colors = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    created = Column(DateTime, index=True, nullable=False)
    crew = Column(Integer, nullable=False)
    edited = Column(DateTime, nullable=False)
    length = Column(Integer, nullable=False)
    manufacturer = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    model = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=False)
    pilots = Column(String(250), nullable=False)
    films = Column(Integer, ForeignKey("films.id"), nullable=False)
    url = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    MGLT = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(Integer, nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    created = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    edited = Column(Integer, nullable=False)
    hyperdrive_rating = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    manufacturer = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    model = Column(Integer, nullable=False)
    name = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    films = Column(Integer, ForeignKey("films.id"), nullable=False)
    pilots = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    characters = Column(Integer, nullable=False)
    created = Column(Integer, nullable=False)
    director = Column(Integer, nullable=False)
    edited = Column(Integer, nullable=False)
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(Integer, nullable=False)
    planets = Column(String(250), nullable=False)
    producer = Column(String(250), nullable=False)
    release_date = Column(Integer, nullable=False)
    species = Column(String(250), nullable=False)
    starships = Column(String(250), nullable=False)
    title = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    vehicles = Column(Integer, ForeignKey("vehicles.id"), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')