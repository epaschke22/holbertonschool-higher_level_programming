#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """base class for other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json list to file"""
        output = []
        if list_objs is not None:
            for obj in list_objs:
                output.append(cls.to_dictionary(obj))
        with open("{}.json".format(cls.__name__), 'w') as file:
            file.write(cls.to_json_string(output))

    @staticmethod
    def from_json_string(json_string):
        """converts json string back to list"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates class instance from dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
        elif cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
        else:
            dummy = cls()
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances from file"""
        output = []
        try:
            with open("{}.json".format(cls.__name__)) as file:
                loaded = cls.from_json_string(file.read())
                for item in loaded:
                    output.append(cls.create(**item))
                return output
        except:
            return output
