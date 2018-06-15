#!/usr/bin/python3
from models.base_model import BaseModel
"""
Here we will be creating a class User that inherits from BaseModel
"""


class User(BaseModel):
    """
    Creating a class named User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        super will initialize and inherit from the parent class(Base_model)/\
        keyworded arguments
        """
        super().__init__(**kwargs)
