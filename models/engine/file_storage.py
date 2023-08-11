#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    serializes instances to a json file and deserializes json file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects in the obj with key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serialized __objects to json file
        """
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes json file to __objects with key
        """
        try:
            with open(self.__file_path, "r") as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, object_id = key.split(".")
                    class_obj = globals()[class_name]
                    object_instance = class_obj(**value)
                    self.__objects[key] = object_instance
        except FileNotFoundError:
            pass
