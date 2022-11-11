#!/usr/bin/python3
"""Test module for the `Amenity class`.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """TestCase for the `Review class`."""

    def setUp(self):
        """setup code."""
        self.my_amenity = Amenity()

    def test_instance(self):
        """test for instances."""
        self.assertTrue(isinstance(self.my_amenity, Amenity))

    def test_issubclass_BaseModel(self):
        """tests if Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.my_amenity), BaseModel))

    def test_name_attr(self):
        """test for public attribute `name`."""
        self.assertTrue(hasattr(self.my_amenity, 'name'))
        self.assertTrue(self.my_amenity.name == '')
        self.assertTrue(self.my_amenity.name == '')


if __name__ == "__main__":
    unittest.main()
