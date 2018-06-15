#!/usr/bin/python3
"""
Review class


"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Creating a state class that inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Intializing the state and passing args
        """
        super().__init__(**kwargs)
