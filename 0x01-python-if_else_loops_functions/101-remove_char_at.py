#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    count = 0
    for i in str:
        if count == n:
            count += 1
            continue
        newstr += i
        count += 1
    return newstr

print(remove_char_at("Holberton School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
