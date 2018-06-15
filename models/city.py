#!/usr/bin/python3
"""
City class


"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Creating a City class that inherits BaseModel
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Intializing the City class and passing arguments
        """
        super().__init__(**kwargs)
