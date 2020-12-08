#!/usr/bin/python3
def fizzbuzz():
    str = ""

    for i in range(1, 101):
        if i % 3 == 0:
            str += "Fizz"
        if i % 5 == 0:
            str += "Buzz"
        if str != "":
            print(str, end='')
            str = ""
        else:
            print(i, end='')
        print(" ", end='')
    print("")
