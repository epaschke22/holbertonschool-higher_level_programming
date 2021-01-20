#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file in json format"""
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
