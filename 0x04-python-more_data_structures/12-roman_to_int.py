#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str or roman_string == "":
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0
    for i in range(0, len(roman_string)):
        if i != len(roman_string) - 1:
            if roman[roman_string[i + 1]] > roman[roman_string[i]]:
                output -= roman[roman_string[i]] * 2
        output += roman[roman_string[i]]
    return output
