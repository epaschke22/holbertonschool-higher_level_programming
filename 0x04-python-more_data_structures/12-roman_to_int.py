#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number_list = []
    for i in roman_string:
        number_list.append(roman[i])
    for i in range(0, len(number_list)):
        try:
            if number_list[i + 1] > number_list[i]:
                number_list[i] *= -1
        except:
            pass
    return sum(number_list)
