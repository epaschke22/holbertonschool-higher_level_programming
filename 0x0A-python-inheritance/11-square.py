#!/usr/bin/python3
"""Example class that uses inheritence"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class based on Rectangle"""
    def __init__(self, size):
        """runs the init from rectangle with size"""
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """returns string when printed"""
        return "[Square] {}/{}".format(self.__size, self.__size)
