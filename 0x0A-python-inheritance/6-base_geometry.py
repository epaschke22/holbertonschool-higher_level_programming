#!/usr/bin/python3
"""Example class to inherit from"""


class BaseGeometry:
    """Geometry class"""
    def area(self):
        """raises exception when not implemented"""
        raise Exception("area() is not implemented")
