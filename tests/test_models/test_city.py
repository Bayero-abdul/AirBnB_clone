#!/usr/bin/python3
"""Test module for the `City class`.
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestReview(unittest.TestCase):
    """TestCase for the `City class`."""

    def setUp(self):
        """setup code."""
        self.my_city = City()

    def test_instance(self):
        """test for instances."""
        self.assertTrue(isinstance(self.my_city, City))

    def test_issubclass_BaseModel(self):
        """tests if Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.my_city), BaseModel))

    def test_state_id_attr(self):
        """test for public attribute `state_id`."""
        self.assertTrue(hasattr(self.my_city, 'state_id'))
        self.assertTrue(self.my_city.state_id == '')
        self.assertEqual(type(self.my_city.state_id), str)

    def test_name_attr(self):
        """test for public attribute `name`."""
        self.assertTrue(hasattr(self.my_city, 'name'))
        self.assertTrue(self.my_city.name == '')
        self.assertEqual(type(self.my_city.name), str)


if __name__ == "__main__":
    unittest.main()
