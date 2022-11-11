#!/usr/bin/python3
"""Test module for the `State class`.
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """TestCase for the `State class`."""

    def setUp(self):
        """setup code."""
        self.my_state = State()

    def test_instance(self):
        """test for instances."""
        self.assertTrue(isinstance(self.my_state, State))

    def test_issubclass_BaseModel(self):
        """tests if State is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.my_state), BaseModel))

    def test_name_attr(self):
        """test for public attribute `name`."""
        self.assertTrue(hasattr(self.my_state, 'name'))
        self.assertTrue(self.my_state.name == '')


if __name__ == "__main__":
    unittest.main()
