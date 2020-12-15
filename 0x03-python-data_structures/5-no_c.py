#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in range(0, len(my_string)):
        if ord(my_string[i]) != 67 and ord(my_string[i]) != 99:
            new_string += my_string[i]
    return(new_string)
