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

    @classmethod
    def setUpClass(self):
        """Code to execute before testing occurs"""
        self.fs = FileStorage()

    @classmethod
    def tearDownClass(self):
        """Code to execute after tests are executed"""
        if os.path.exists("file.json"):
            os.remove("file.json")

        FileStorage._FileStorage__objects = {}

    def test_IsFileStorage(self):
        """test for instances of FileStorage."""
        self.assertIsInstance(FileStorage(), FileStorage)


    def test_has_file_path_attr(self):
        """test if private class attribute __file_path
        exits.
        """
        self.assertTrue(hasattr(FileStorage(), '_FileStorage__file_path'))
        self.assertFalse(hasattr(FileStorage(), '__file_path'))

        with self.assertRaises(TypeError):
            self.fs._FileStorage__file_path()

    def test_has_objects_attr(self):
        """test if private class attribute __objects exists.
        """
        self.assertTrue(hasattr(FileStorage(), '_FileStorage__objects'))
        self.assertFalse(hasattr(FileStorage(), '__objects'))
        self.assertIs(type(self.fs._FileStorage__objects), dict)
        self.assertTrue(self.fs._FileStorage__objects == {})

        with self.assertRaises(TypeError):
            self.fs._FileStorage__objects()

    def test_all(self):
        """test if all() returns a dictionary"""
        self.assertTrue(hasattr(self.fs, 'all'))
        self.assertIsInstance(self.fs.all(), dict)
        self.assertTrue(self.fs._FileStorage__objects == {})

        # test for arg passed
        with self.assertRaises(TypeError):
            self.fs.all(None)

    def test_new(self):
        """test for new() function."""
        self.assertTrue(hasattr(self.fs, 'new'))

        my_model = BaseModel()
        self.assertIn("BaseModel." + my_model.id, storage.all().keys())
        self.assertTrue(dir(my_model) == dir(BaseModel()))

        with self.assertRaises(AttributeError):
            diff_types = [1, 'string', [34, 6], {'hello': 7}, (3, 6), True, None]
            for diff_type in diff_types:
                self.fs.new(diff_type)

        with self.assertRaises(TypeError):
            storage.new(my_model, 45)

    def test_save(self):
        """test for save() function."""
        my_model = BaseModel()
        b_updated_at = my_model.updated_at
        my_model.save()
        self.assertTrue(b_updated_at != my_model.updated_at)
        self.assertTrue(hasattr(self.fs, 'save'))

        """test if __file_path exists"""
        self.assertTrue(os.path.exists('file.json'))

        with self.assertRaises(TypeError):
            self.fs.save(1)


if __name__ == "__main__":
    unittest.main()
