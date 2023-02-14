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
