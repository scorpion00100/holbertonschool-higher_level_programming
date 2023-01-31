#!/usr/bin/python3
"""
Defines class Square with private attribute
"""
class Square:
    """
    size : size of side in square
    """
    def __init__(self, size = 0):
        """
        Initialize square
        """
        if type(size) is not int:
            raise TypeError("size mut be an integer")
        elif size < 0:
            raise ValueError("size mut be >= 0")
        else:
            self__size = size
