#!/usr/bin/python3
"""
Place class


"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Creating a class named Place that inherits the BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Intializing the Place class and passing arguments
        """
        super().__init__(**kwargs)
