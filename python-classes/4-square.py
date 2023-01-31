#!/usr/bin/python3
"""
Defines class Square with private attribute size and validates size
"""


class Square:
    """
    size (int): size of a side in square
    """

    def __init__(self, size=0):
        """
        Initialize square
        """
    @property
    def size(self):
        return self.__size
        
    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size)**2
