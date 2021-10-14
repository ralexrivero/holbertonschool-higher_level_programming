#!/usr/bin/python3
"""Student class documentation"""


class Student:

    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
            Instantiation function for Student
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Returns a dictionary thats represents:
            - an object or
            - a dictionary
        Args:
            attrs (list): attributes
        Returns:
            A dictionary that represent the objetc
        """

        if not isinstance(attrs, list):
            return self.__dict__
        for var in attrs:
            if not isinstance(var, str):
                return self.__dict__
        string_dict = {}
        for string in attrs:
            if string in self.__dict__.keys():
                string_dict[string] = self.__dict__[string]
        return string_dict
