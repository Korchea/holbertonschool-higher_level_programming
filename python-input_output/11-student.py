#!/usr/bin/python3
"""Student

    Returns:
        JSON: Return a JSON class
"""


class Student():
    """Student
    """

    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            aux = {}
            for a in attrs:
                if a == "first_name":
                    aux.update({a: self.first_name})
                elif a == "last_name":
                    aux.update({a: self.last_name})
                elif a == "age":
                    aux.update({a: self.age})
            myKeys = list(aux.keys())
            myKeys.sort()
            sorted_dict = {i: aux[i] for i in myKeys}
            return sorted_dict

    def reload_from_json(self, json):
        self.age = json['age']
        self.last_name = json['last_name']
        self.first_name = json['first_name']
