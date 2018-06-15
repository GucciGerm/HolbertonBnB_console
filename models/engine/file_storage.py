#!/usr/bin/python3
"""
FileStorage Model


"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    Stores Python dictionaries as JSON files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        All will print the string representation of all instances
        """
        return (self.__objects)

    def new(self, obj):
        """
        New will insert an object into the __objects dictiionary
        """
        self.__objects.update({"{}.{}".format(obj.__class__.__name__,
                                              obj.id): obj})

    def save(self):
        """
        Save will serialize an object in __objects to the JSON file format
        """
        d1 = {}
        with open(self.__file_path, mode="w") as f:
            for k, v in self.__objects.items():
                d1[k] = v.to_dict()
            json.dump(d1, f)

    def reload(self):
        """
        Reload will deserialize a JSON formatted file to an __object
        *** Only if it exists!
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r") as f:
                readit = json.load(f)
                for v in readit.values():
                    a = eval("{}(**v)".format(v["__class__"]))
                    self.new(a)
