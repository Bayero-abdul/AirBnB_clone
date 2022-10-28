#!/usr/bin/python3
"""this module contain ``FileStorage`` class that serializes \
instances to a JSON file and deserializes JSON file to instances.
"""

import json, os.path

class FileStorage:
    """serializes instances to a JSON file and deserializes \
        JSON file to instances."""

    def __init__(self):
        """initializes the instances."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the __objects."""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        key = class_name + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            self.__objects = json.loads(f.read())
            for obj_id, value in self.__objects.items():
                obj_id_lst = obj_id.split(".")
                self.__objects[obj_id] = "[{}] ({}) {}".format(obj_id_lst[0], obj_id_lst[1], value)
