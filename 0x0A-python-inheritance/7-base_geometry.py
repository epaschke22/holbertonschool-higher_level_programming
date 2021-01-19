#!/usr/bin/python3
"""Example class to inherit from"""


class BaseGeometry:
    """Geometry class"""
    def area(self):
        """raises exception when not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """makes sure the input is correct"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
