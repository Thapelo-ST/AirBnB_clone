#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    user class inheriting from Base Mode;
    """
    def __init__(self, *args, **kwargs):
        """
        init method for users class
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
