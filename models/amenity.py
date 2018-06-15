#!/usr/bin/python3
"""
Amenity class


"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Creating a class named Amenity that inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializing the Amenity class and passing arguments
        """
        super().__init__(**kwargs)
