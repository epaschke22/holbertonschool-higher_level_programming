#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """checks to make sure input is string and replaces characters"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    t = text.replace(". ", ".").replace("? ", "?").replace(": ", ":")
    t2 = t.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n")
    print(t2, end="")
