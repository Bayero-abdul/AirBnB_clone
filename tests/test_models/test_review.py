#!/usr/bin/python3
"""Test module for the `Review class`.
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """TestCase for the `Review class`."""

    def setUp(self):
        """setup code."""
        self.my_review = Review()

    def test_instance(self):
        """test for instances."""
        self.assertTrue(isinstance(self.my_review, Review))

    def test_issubclass_BaseModel(self):
        """tests if Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.my_review), BaseModel))

    def test_place_id_attr(self):
        """test for public attribute `place_id`."""
        self.assertTrue(hasattr(self.my_review, 'place_id'))
        self.assertTrue(self.my_review.place_id == '')

    def test_user_id_attr(self):
        """test for public attribute `user_id`."""
        self.assertTrue(hasattr(self.my_review, 'user_id'))
        self.assertTrue(self.my_review.user_id == '')

    def test_text_attr(self):
        """test for public attribute `text`."""
        self.assertTrue(hasattr(self.my_review, 'text'))
        self.assertTrue(self.my_review.text == '')


if __name__ == "__main__":
    unittest.main()
