#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """returns dictionary description for json object"""
    return vars(obj)
