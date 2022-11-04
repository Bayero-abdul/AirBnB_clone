#!/usr/bin/python3
"""
This module contains a ``BaseModel`` class that defines \
all common attributes/methods for other classes.
"""

import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """defines all commom attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Instantiates instances of an object."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """string representaion of the instances."""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def save(self):
        """Updates the updated_at date."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of \
         __dict__ of the instance."""
        from copy import deepcopy
        to_dict = deepcopy(self.__dict__)
        to_dict['__class__'] = self.__class__.__name__
        for key in self.__dict__:
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                to_dict[key] = value
        return to_dict
