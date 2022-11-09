#!/usr/bin/python3
"""Module contains tests for file storage.
"""

import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class."""

    # setUp and tearDown function reference:
    # https://github.com/betascribbles/AirBnB_clone/blob/
    # main/tests/test_models/test_engine/test_file_storage.py

    def setUp(self):
        """Code to execute before testing occurs"""
        try:
            os.path.exists("file.json")
        except IOError:
            pass

    def tearDown(self):
        """Code to execute after tests are executed"""
        # Remove file.json if it exists
        try:
            os.remove("file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_IsFileStorage(self):
        """test for instances of FileStorage."""
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_has_file_path_attr(self):
        """test if private class attribute __file_path
        exits.
        """
        self.assertFalse(hasattr(FileStorage(), '__file_path'))

    def test_has_objects_attr(self):
        """test if private class attribute __objects exists.
        """
        self.assertFalse(hasattr(FileStorage(), '__objects'))

    def test_all(self):
        """test if all() returns a dictionary"""
        self.assertIsInstance(storage.all(), dict)

        # test for arg passed
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        """test for new() function."""
        my_model = BaseModel()
        self.assertIn("BaseModel." + my_model.id, storage.all().keys())

        with self.assertRaises(TypeError):
            storage.new(my_model, 45)

        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save(self):
        """test for save() function."""
        my_model = BaseModel()
        b_updated_at = my_model.updated_at
        my_model.save()

        self.assertTrue(b_updated_at != my_model.updated_at)


if __name__ == "__main__":
    unittest.main()
