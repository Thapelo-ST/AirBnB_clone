#!/usr/bin/python3
"""
    base model the class that will be the main class for the whole project
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    base model class to initialise all methods and variables needed in the project
    """

    def save(self):
        """
        updates the time the instance was created at or modified
        """
        # from models.__init__ import storage
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def __init__(self, *args, **kwargs):
        """
        init method
        """
        if kwargs:
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "__class__" in kwargs:
                del kwargs["__class__"]
            self.__dict__.update(kwargs)
            from models.__init__ import storage
            # from models import storage
            storage.new(self)
        else:
            # from models import storage
            from models.__init__ import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
            storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary['id'] = self.id
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """
        magic method for printing
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
