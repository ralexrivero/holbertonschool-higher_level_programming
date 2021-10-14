#!/usr/bin/python3
"""Student function documentation"""


class Student:
    """
    defines a student by:
        Public instance attributes:
            first_name
            last_name
            age
"""
    def __init__(self, first_name, last_name, age):
        """Initializes instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Retrieves the dictionary
        """
        return self.__dict__
