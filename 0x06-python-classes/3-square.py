#!/usr/bin/python3
"""This is a example class"""


class Square:
    """This is a class with a private feild"""
    def __init__(self, size=0):
        """This initializes the size feild"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method finds the square area"""
        return self.__size * self.__size
