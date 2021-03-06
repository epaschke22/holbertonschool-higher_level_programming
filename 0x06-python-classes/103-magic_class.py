#!/usr/bin/python3
"""This is decoded from ByteCode"""
import math


class MagicClass:
    """MAGIC CLASS"""
    def __init__(self, radius):
        """doc string 1"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
            self.__radius = None

    def area(self):
        """doc string 2"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """doc string 3"""
        return 2 * self.__radius * math.pi
