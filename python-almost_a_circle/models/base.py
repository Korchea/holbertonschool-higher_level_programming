#!/usr/bin/python3
"""Base
"""
import json


class Base():
    """Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """to_json_string

        Args:
            list_dictionaries (list)

        Returns:
            dict
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return []
        else:
            return json.dumps(list_dictionaries)
