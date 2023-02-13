#!/usr/bin/python3
"""Module for Recatngle"""
from models.base import Base



class Rectangle(Base):
    """
    Class that represents a Rectangle and inherits from Base.

    Private instance attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
        __x (int): x-coordinate of the rectangle
        __y (int): y-coordinate of the rectangle

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): id of the rectangle. Defaults to None.

        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: width of the rectangle.
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): new value for the width attribute.
        """
        self.__width = value
    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: height of the rectangle.
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): new value for the height attribute.
        """
        self.__height = value
    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
            int: x-coordinate of the rectangle.
        """
        return self.__x
    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): new value for the x attribute.
        """
        self.__x = value
    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
            int: y-coordinate of the rectangle.
        """
        return self.__y
    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): new value for the y attribute.
        """
        self.__y = value
