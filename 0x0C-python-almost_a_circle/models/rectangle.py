#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class inherited from base"""
    def __init__(self, width=None, height=None, x=0, y=0, id=None):
        """init method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of Rectangle"""
        return self.width * self.height

    def display(self):
        """prints out rectangle with # symbols"""
        display_str = ""
        for i in range(self.y):
            display_str += "\n"
        for i in range(self.height):
            for j in range(self.x):
                    display_str += " "
            for j in range(self.width):
                display_str += str("#")
            display_str += "\n"
        print(display_str[:-1])

    def __str__(self):
        """returns string message on rectangle stats"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates rectangle attributes"""
        if args is not None and len(args) != 0:
            atts = ['id', 'width', 'height', 'x', 'y']
            for i in range(0, len(args)):
                setattr(self, atts[i], args[i])
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        output = {}
        output["x"] = self.x
        output["y"] = self.y
        output["id"] = self.id
        output["width"] = self.width
        output["height"] = self.height
        return output
