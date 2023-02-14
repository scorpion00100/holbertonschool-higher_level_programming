#!/usr/bin/python3
"""Module for class Base"""
import json


class Base:
    """Parent class in the project"""

    # Number objects created
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor Base class"""
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert dictionary into json string"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of object in a json file"""
        dicts = []
        if list_objs:
            for ins in list_objs:
                dicts.append(cls.to_dictionary(ins))

        json_string = Base.to_json_string(dicts)
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(json_string)   
