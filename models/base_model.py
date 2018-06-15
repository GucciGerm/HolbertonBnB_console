#!/usr/bin/python3
"""
Base class


"""
import uuid
from datetime import datetime as dt
import models


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Creating attributes
        id - Generated a str converted Unique id
        created_at - assign with the current datetime when instance is created
        updated_at - assigning the updated the datetime everytime
        object is changed
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    setattr(self, k, dt.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    pass
                else:
                    setattr(self, k, v)

    def __str__(self):
        """
        __str__ - Here we are returning [{}] ({}) <{}>
        field 1 - class (BaseModel)
        field 2 - id (1234574587453)
        field 3 - dict (dictionary)
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        save - Updating the public instance attribute
        update_at with current datetime
        """
        self.updated_at = dt.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        to_dict - Here we return a copy of the dictionary
        that contains all keys/values of the current dictionary
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ["created_at", "updated_at"]:
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return (dict_1)
