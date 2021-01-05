#!/usr/bin/python3
"""This is a example class"""


class Square:
    """This is a class with a private feild"""
    def __init__(self, size=0, position=(0, 0)):
        """This initializes the size feild"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter function"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter function"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method finds the square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints out a square"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for k in range(self.__position[0]):
                    print("_", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
