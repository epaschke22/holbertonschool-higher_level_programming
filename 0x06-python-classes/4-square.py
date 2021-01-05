#!/usr/bin/python3
"""This is a example class"""


class Square:
    """This is a class with a private feild"""
    def __init__(self, size=0):
        """This initializes the size feild"""
        self.__size = size

    @property
    def size(self):
        """Getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method finds the square area"""
        return self.__size * self.__size
