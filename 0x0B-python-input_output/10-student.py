#!/usr/bin/python3
"""Student to JSON with filter """


class Student:
    """class to beturned into json file"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary of class to json"""
        if attrs is None or type(attrs) is not list:
            return vars(self)
        else:
            new_dict = {}
            for key in attrs:
                if type(key) is str:
                    try:
                        new_dict[key] = self.__dict__[key]
                    except:
                        pass
            return new_dict
