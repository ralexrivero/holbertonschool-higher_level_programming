#!/usr/bin/python3
"""`Square` class defination"""
from .rectangle import Rectangle


class Square(Rectangle):
    """inherits from `Rectangle` class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance attributes
        Args:
            size (int)
            x (int)
            y (int)
            id (int)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square"""
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Retrieves the value of `size`
        """
        return self.width

    @size.setter
    def size(self, value):
        """sets the dimensions of `Square`"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the class"""
        if args and len(args) > 0:
            keys = ["id", "size", "x", "y"]
            for i, j in enumerate(args):
                setattr(self, keys[i], j)
        else:
            for k, j in kwargs.items():
                setattr(self, k, j)

    def to_dictionary(self):
        """Retrieves all the attributes of class to dictionary
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
