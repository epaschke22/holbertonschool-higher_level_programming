#!/usr/bin/python3
"""checks if object is subclass of class"""


def inherits_from(obj, a_class):
    """does not return true it obj and class are same"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
