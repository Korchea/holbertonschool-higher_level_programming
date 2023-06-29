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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string

        Args:
            list_dictionaries (list)

        Returns:
            dict
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        name = "{}.json".format(cls.__name__)
        list_to_save = []
        if list_objs is not None:
            for i in list_objs:
                list_to_save.append(i.to_dictionary())
        with open(name, 'w') as file:
            file.write(cls.to_json_string(list_to_save))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string

        Args:
            json_string (dict):

        Returns:
            str:
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file

        Returns:
            list: Is a list of instances
        """
        name = "{}.json".format(cls.__name__)
        with open(name, 'r') as file:
            f = file.read()
        f_cls = cls.from_json_string(f)
        list = []
        for i in range(len(f_cls)):
            list.append(cls.create(**f_cls[i]))
        return list
