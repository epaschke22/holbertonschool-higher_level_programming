#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts line of text after each line that contains string"""
    with open(filename, 'r+') as fd:
        contents = fd.readlines()
        if search_string in contents[-1]:
            contents.append(new_string)
        else:
            for index, line in enumerate(contents):
                if search_string in line:
                    contents.insert(index + 1, new_string)
        fd.seek(0)
        fd.writelines(contents)
