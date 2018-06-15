#!/usr/bin/python3
"""
Review class


"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Creating a class named Review that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Here we are initializing the Review class and passing the arguments
        """
        super().__init__(**kwargs)
