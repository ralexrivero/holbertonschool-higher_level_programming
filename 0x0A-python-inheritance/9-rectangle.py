#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:

    """Base Geometry class empty"""

    def area(self):
        """Area function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer value
        Args:
            name (str): string name
            value (int): value to be validated
        Raises:
            TypeError: if not an integer
            ValueError: if less or equal to 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    """Rectangle class inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiation function
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area function
        Returns:
            Rectangle area
        """

        return self.__width * self.__height

    def __str__(self):
        """The function for print and str
        Returns:
            Specially formated string
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
