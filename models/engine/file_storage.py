#!/usr/bin/python3
"""this module contain ``FileStorage`` class that serializes \
instances to a JSON file and deserializes JSON file to instances.
"""

import json
import os.path


class FileStorage:
    """serializes instances to a JSON file and deserializes \
JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        key = class_name + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for key, value in self.__objects.items():
                self.__objects[key] = value.to_dict()
            f.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                read = json.loads(f.read())
                for key, value in read.items():
                    self.__objects[key] = BaseModel(**value)
