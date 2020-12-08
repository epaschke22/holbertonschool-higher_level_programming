#!/usr/bin/python3
def fizzbuzz():
    result = ""
    fb = ""
    for i in range(1, 101):
        if i % 3 == 0:
            fb += "Fizz"
        if i % 5 == 0:
            fb += "Buzz"
        if fb != "":
            result += fb
            fb = ""
        else:
            result += str(i)
        result += " "
    print(result)
