#!/usr/bin/python3
"""define class Square"""


class Square:
    """Defines a square:"""

    def __init__(self, size=0):
        """Initializer object"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
