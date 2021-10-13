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
            rectangle area
        """

        return self.__width * self.__height

    def __str__(self):
        """The function for print and str
        Returns:
            Specially formated string
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):

    """Square class that inherits from Rectangle subclass which inherits
       from BaseGeometry class"""

    def __init__(self, size):
        """Instantiation function for size attribute
        Args:
            size (int): the size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area function for the square object
        Returns:
            Area of the square
        """

        return self.__size ** 2
