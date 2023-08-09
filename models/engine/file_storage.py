#!/usr/bin/python3
"""

"""
import json


class FileStorage:
    """
    a class to handle serialization and deserialization of instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in objects the object with key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes objects to the JSON file
        """
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, object_id = key.split(".")
                    class_obj = globals()[class_name]
                    object_instance = class_obj(**value)
                    FileStorage.__objects[key] = object_instance
        except FileNotFoundError:
            pass

