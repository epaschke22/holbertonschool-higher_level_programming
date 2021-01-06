#!/usr/bin/python3
"""This is a example class"""


class Square:
    """This is a class with a private field"""
    def __init__(self, size=0, position=(0, 0)):
        """This initializes the size and position field"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter size function"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter size function"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter position function"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter position function"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This method finds the square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints out a square with an offset"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")

    def __str__(self):
        """returns object as square"""
        square_str = ""
        if self.__size == 0:
            square_str = "\n"
        else:
            for i in range(self.__position[1]):
                square_str += "\n"
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    square_str += " "
                for j in range(self.__size):
                    square_str += "#"
                square_str += "\n"
        return square_str[:-1]
