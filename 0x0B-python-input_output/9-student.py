#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """class to beturned into json file"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary of class to json"""
        return vars(self)
