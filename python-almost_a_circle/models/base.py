#!/usr/bin/python3
"""Module for class Base"""
import json


class Base:
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objectis

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
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

    @staticmethod
    def from_json_string(json_string):
        """Return list Pyhton objects from json_string"""
        if not json_string:
            return []

        return json.loads(json_string)
