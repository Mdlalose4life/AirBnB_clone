#!/usr/bin/python3
"""FileStorage Class
serializes instances to a JSON file
and deserializes JSON file to Instances
"""
import json
import uuid
import sys
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
    
    dict0 = {
        "BaseModel": BaseModel,
        "Amenity": Amenity,
        "User": User
    }
    
    dict1 = {
        "State": State,
        "City": City,
        "Review": Review,
        "Place": Place
    }
    
    dict0.update(dict1)
    
    def all(self):
        """returns the dict representation of '__objects'"""
        return FileStorage.__objects
    
    def new(self, obj_key):
        """sets in '__objects the object with key '<obj class name>.id"""
        each_key = f"{type(obj_key).__name__}.{obj.id}"
        FileStorage.__objects[each_key] = obj_key
        
    def save(self):
        """Serializes '__objects into a JSON file"""
        
        serialze_dict = {}
        
        for each_key, each_value in FileStorage.__objects.iterm():
            serialze_dict[each_key] = each_value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialze_dict, file)
            
    def reload(self):
        """Deserializes the JSON file to __objects"""
        
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                for each_key, each_value in FileStorage.__objects.iterm():
                    obj_key = FileStorage.__objects
                    obj_key[each_key] = FileStorage.dict[each_value["__class__"]](**each_value)
