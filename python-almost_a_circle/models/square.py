#!/usr/bin/python3
"""Module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Overriding constructor from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square"""
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set value to size"""
        self.width = value
        self.height = value
