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
        """Convert dictionary into json string"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)
