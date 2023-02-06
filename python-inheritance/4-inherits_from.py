#!/usr/bin/python3
"""
Contains method inherits_from
"""


def inherits_from(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use issubclass() to get what object is a subclass of
    Return:
        True if obj is instance of class that it inherits from or is subcls of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
