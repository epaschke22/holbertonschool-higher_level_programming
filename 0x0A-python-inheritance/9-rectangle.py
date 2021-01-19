#!/usr/bin/python3
"""Example class that uses inheritence"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """initialize method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns width * height"""
        return self.__width * self.__height

    def __str__(self):
        """returns string when printed"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
