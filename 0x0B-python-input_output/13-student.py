#!/usr/bin/python3
"""Student class documentation"""


class Student:

    """
        The Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Instatiation function for Student class
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary
        Args:
            attrs (list): attributes to include
        Returns:
            dictionary representing the object
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

    def reload_from_json(self, json):
        """replaces all attributes into Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
