#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    output = {}
    for i in a_dictionary.keys():
        output[i] = a_dictionary[i] * 2
    return output
