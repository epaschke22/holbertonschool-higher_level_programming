#!/usr/bin/python3
"""Load, add, save """
from sys import argv

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    file = load(filename)
except:
    with open(filename, 'w'):
        file = []
file += argv[1:]
save(file, filename)
