#!/usr/bin/python3
"""Test module for the `Place class`.
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestReview(unittest.TestCase):
    """TestCase for the `Place class`."""

    def setUp(self):
        """setup code."""
        self.my_place = Place()

    def test_instance(self):
        """test for instances."""
        self.assertTrue(isinstance(self.my_place, Place))

    def test_issubclass_BaseModel(self):
        """tests if Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.my_place), BaseModel))

    def test_city_id_attr(self):
        """test for public attribute `city_id`."""
        self.assertTrue(hasattr(self.my_place, 'city_id'))
        self.assertTrue(self.my_place.city_id == '')
        self.assertEqual(type(self.my_place.city_id), str)

    def test_user_id_attr(self):
        """test for public attribute `user_id`."""
        self.assertTrue(hasattr(self.my_place, 'user_id'))
        self.assertTrue(self.my_place.user_id == '')
        self.assertEqual(type(self.my_place.user_id), str)

    def test_name_attr(self):
        """test for public attribute `name`."""
        self.assertTrue(hasattr(self.my_place, 'name'))
        self.assertTrue(self.my_place.name == '')
        self.assertEqual(type(self.my_place.name), str)

    def test_description_attr(self):
        """test for public attribute `description`."""
        self.assertTrue(hasattr(self.my_place, 'description'))
        self.assertTrue(self.my_place.description == '')
        self.assertEqual(type(self.my_place.description), str)

    def test_number_rooms_attr(self):
        """test for public attribute `number_rooms`."""
        self.assertTrue(hasattr(self.my_place, 'number_rooms'))
        self.assertTrue(self.my_place.number_rooms == 0)
        self.assertEqual(type(self.my_place.number_rooms), int)

    def test_number_bathrooms_attr(self):
        """test for public attribute `number_bathrooms`."""
        self.assertTrue(hasattr(self.my_place, 'number_bathrooms'))
        self.assertTrue(self.my_place.number_bathrooms == 0)
        self.assertEqual(type(self.my_place.number_bathrooms), int)

    def test_max_guest_attr(self):
        """test for public attribute `max_guest`."""
        self.assertTrue(hasattr(self.my_place, 'max_guest'))
        self.assertTrue(self.my_place.max_guest == 0)
        self.assertEqual(type(self.my_place.max_guest), int)

    def test_price_by_night_attr(self):
        """test for public attribute `price_by_night`."""
        self.assertTrue(hasattr(self.my_place, 'price_by_night'))
        self.assertTrue(self.my_place.price_by_night == 0)
        self.assertEqual(type(self.my_place.price_by_night), int)

    def test_latitude_attr(self):
        """test for public attribute `latitude`."""
        self.assertTrue(hasattr(self.my_place, 'latitude'))
        self.assertTrue(self.my_place.latitude == 0.0)
        self.assertEqual(type(self.my_place.latitude), float)

    def test_longitude_attr(self):
        """test for public attribute `longitude`."""
        self.assertTrue(hasattr(self.my_place, 'longitude'))
        self.assertTrue(self.my_place.longitude == 0.0)
        self.assertEqual(type(self.my_place.longitude), float)

    def test_amenity_ids_attr(self):
        """test for public attribute `amenity_ids`."""
        self.assertTrue(hasattr(self.my_place, 'amenity_ids'))
        self.assertTrue(self.my_place.amenity_ids == [])
        self.assertEqual(type(self.my_place.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
