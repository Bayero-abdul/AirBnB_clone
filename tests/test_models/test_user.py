#!/usr/bin/python3
"""
Test for the user class.
"""

import os
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """TestCase for the User Class."""

    def setUp(self):
        """the set-up code."""
        self.my_user = User()
        self.my_user.first_name = "Betty"
        self.my_user.last_name = "Bar"
        self.my_user.email = "airbnb@mail.com"
        self.my_user.password = "root"

    def tearDown(self):
        """tears down the setup code."""
        if (os.path.exists('file.json')):
            os.remove('file.json')

    def test_isUser(self):
        """test for instances of User"""
        self.assertIs(type(self.my_user), User)

    def test_idtype(self):
        """test if id is of string type."""
        self.assertIs(type(self.my_user.id), str)

    def test_typecreated_at(self):
        """test if created_at is of datetime type"""
        self.assertIs(type(self.my_user.created_at), datetime)

    def test_typeupdated_at(self):
        """test if updated_at is of datetime type"""
        self.assertIs(type(self.my_user.updated_at), datetime)

    def test_public_cls_attr_first_name(self):
        """test if first name is a public class attribute."""
        self.assertTrue(hasattr(self.my_user, 'first_name'))

    def test_public_cls_attr_last_name(self):
        """test if last name is a public class attribute."""
        self.assertTrue(hasattr(self.my_user, 'last_name'))

    def test_public_cls_attr_email(self):
        """test if email is a public class attribute."""
        self.assertTrue(hasattr(self.my_user, 'email'))

    def test_public_cls_attr_password(self):
        """test if password is a public class attribute."""
        self.assertTrue(hasattr(self.my_user, 'password'))
    
    def test_types_public_cls_attr(self):
        """test if the public class attributes values \
are strings.:"""
        self.assertIs(type(self.my_user.first_name), str)
        self.assertIs(type(self.my_user.last_name), str)
        self.assertIs(type(self.my_user.email), str)
        self.assertIs(type(self.my_user.password), str)

    def test_save(self):
        """test the save() method."""
        updated_at_before_save = self.my_user.updated_at
        self.my_user.save()
        self.assertTrue(updated_at_before_save != self.my_user.updated_at)

        self.assertTrue(os.path.exists('file.json'))

        with self.assertRaises(TypeError):
            self.my_user(None)

    def test_to_dict(self):
        """Test if to_dict() returns a dictionary."""
        my_user_json = self.my_user.to_dict()
        self.assertIs(type(my_user_json), dict)

        with self.assertRaises(TypeError):
            self.my_user.to_dict(None, 1)

    def test__str__(self):
        """Test for the string representation."""
        self.assertEqual(str(self.my_user), "[User] ({}) {}"
                         .format(self.my_user.id, self.my_user.__dict__))

    def test_to_dict_has_class_attr(self):
        """Test if to_dict() has __class__ attribute."""
        my_user_json = self.my_user.to_dict()
        self.assertTrue(hasattr(my_user_json, '__class__'))

    def test_to_dict_output(self):
        """Test to_dict output."""
        u = User()
        dt = datetime.now()
        u.id = "12345"
        u.created_at = u.updated_at = dt
        u.first_name = "Betty"
        u.last_name = "Bar"
        u.email = "airbnb@mail.com"
        u.password = "root"
        test_dict = {
            'id': "12345",
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
            '__class__': 'User',
            'first_name': "Betty",
            'last_name': "Bar",
            'email': "airbnb@mail.com",
            'password': "root"
        }
        self.assertDictEqual(test_dict, u.to_dict())

    def test_uniqueid(self):
        """Test if id of different instances is different."""
        my_user_1 = User()
        self.assertTrue(my_user_1.id != self.my_user.id)


if __name__ == "__main__":
    unittest.main()
