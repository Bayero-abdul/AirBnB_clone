#!/usr/bin/python3
"""
This module contains a ``BaseModel`` class that defines \
all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """defines all commom attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Instantiates instances of an object."""

        if kwargs:
            self.set_attributes(kwargs)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def set_attributes(self, kwargs):
        """set obj attributes from key/values."""
        for key, value in kwargs.items():
            if key != '__class__':
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        """string representaion of the instances."""
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """Updates the updated_at date."""
        storage.save()
        #self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values of \
         __dict__ of the instance."""
        to_dict = self.__dict__
        to_dict['__class__'] = self.__class__.__name__
        to_dict['created_at'] = self.created_at.isoformat()
        to_dict['updated_at'] = self.updated_at.isoformat()
        return to_dict
