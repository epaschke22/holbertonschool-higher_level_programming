#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    output = 0
    for key, value in a_dictionary.items():
        if value > output:
            output = value
    return output
