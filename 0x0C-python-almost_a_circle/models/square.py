#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class based on Rectangle"""
    def __init__(self, size=None, x=0, y=0, id=None):
        """init method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returns string message on square stats"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """updates square attributes"""
        if args is not None and len(args) != 0:
            atts = ['id', 'size', 'x', 'y']
            for i in range(0, len(args)):
                setattr(self, atts[i], args[i])
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns dictionary representation of square"""
        output = {}
        output["x"] = self.x
        output["y"] = self.y
        output["id"] = self.id
        output["size"] = self.size
        return output
