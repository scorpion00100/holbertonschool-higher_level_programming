#!/usr/bin/python3
"""Module for class Base"""
import json
import os.path


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
        """ list of dictionaries to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)
