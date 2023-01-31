#!/usr/bin/python3
"""
Defines class Square with private attribute
"""
class Square:
    """
    size : size of side in square
    """
    def __init__(self, size = 0):
        try:
            self.__size = int(size)
        except TypeError:
            print("size must be an integer")
        if size < 0:
            except ValueError:
                print("size must be >= 0")
