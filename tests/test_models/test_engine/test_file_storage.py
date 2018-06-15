#!/usr/bin/python3
"""
Unittests for file_storage
"""
import os
import sys
import pep8
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage


class Test_File_Storage(unittest.TestCase):
    """
    Test cases
    """
    def test_docstr(self):
        """
        Checks for comments
        """
        self.assertTrue(len(models.storage.__doc__) > 1)
        self.assertTrue(len(models.storage.all.__doc__) > 1)
        self.assertTrue(len(models.storage.new.__doc__) > 1)
        self.assertTrue(len(models.storage.save.__doc__) > 1)
        self.assertTrue(len(models.storage.reload.__doc__) > 1)

    def test_pep8(self):
        """
        Checks for pep8 styling
        """
        style = pep8.StyleGuide(quiet=True)
        pycode = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(pycode.total_errors, 0, "fix pep8")

    @classmethod
    def setup_user(cls):
        """
        Checks User class configurations
        """
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.user.email = "HBNB@Holbie.com"
        cls.storage = FileStorage()

    @classmethod
    def tearDown(cls):
        """
        Removes User class test
        """
        del cls.user

    def tearDown(self):
        """
        Removes JSON file created in storage
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Tests the all method
        """
        fs = FileStorage()
        dict_1 = fs.all()
        self.assertIsNotNone(dict_1)
        self.assertEqual(type(dict_1), dict)
        self.assertIs(dict_1, fs._FileStorage__objects)

    def test_new(self):
        """
        Tests the new method
        """
        new_fs = FileStorage()
        dict_2 = new_fs.all()
        Holbie = User()
        Holbie.id = 8888
        Holbie.name = "Dennis"
        new_fs.new(Dennis)
        key = new_fs.__class__.__name__ + "." + str(new_fs.id)
        self.assertIsNotNone(dict_2[key])

    def test_reload(self):
        """
        Tests the reload method
        """
        new_fs = FileStorage()

        try:
            os.remove("file.json")
        except:
            pass

        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for item in f:
                self.assertEqual(item, "{}")
        self.assertIs(new_fs.reload(), None)
