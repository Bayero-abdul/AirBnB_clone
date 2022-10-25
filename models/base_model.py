#!/usr/bin/python3
"""
This module contains a ``BaseModel`` class that defines \
all common attributes/methods for other classes
"""

import uuid
from datetime import datetime


class BaseModel:
    """defines all commom attributes/methods for other classes.""" 
    def __init__(self):
        """Instantiates instances of an object."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """string representaion of the instances."""
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
    
    def save(self):
        """Updates the updated_at date."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values of \
         __dict__ of the instance."""
        to_dict = self.__dict__
        to_dict['__class__'] = self.__class__.__name__
        to_dict['created_at'] = self.created_at.isoformat()
        to_dict['updated_at'] = self.updated_at.isoformat()
        return to_dict
