#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    name = ""
    age = 0
    for key, value in a_dictionary.items():
        if value > age:
            age = value
            name = key
    return name
