#!/usr/bin/python3
"""FileStorage Class
serializes instances to a JSON file
and deserializes JSON file to Instances
"""
import json
import uuid
import os
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes and deserializes instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict representation of '__objects'"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in '__objects the object with key '<obj class name>.id"""
        each_key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(each_key, obj.id)] = obj

    def save(self):
        """Serializes '__objects into a JSON file"""
        serialze_dict = FileStorage.__objects
        ser_dict = {obj: serialze_dict[obj].to_dict() for obj in ser_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(ser_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                ser_dict = json.load(f)
                for o in ser_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
