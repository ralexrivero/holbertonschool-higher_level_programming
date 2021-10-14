#!/usr/bin/python3
"""Student class documentation"""


class Student:

    """The Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation function for Student class
            defines a student by: (based on 10-student.py)
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary of the instance
        Returns:
            dictionary of the instance
        """

        return self.__dict__
