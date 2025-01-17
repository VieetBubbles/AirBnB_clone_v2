#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from os import getenv
from models.place import Place


class Amenity(BaseModel, Base):
    """This is the class for Amenities
    Attributes:
        name: name input
        place_amenities: list of Amenity ids
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship("Place", secondary=Place.place_amenity,
                                       back_populates='amenities',
                                       viewonly=False)
