#!/usr/bin/python3
"""function that adds attributes only if they exist"""


def add_attribute(obj, name, value):
    """checks for object first"""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
