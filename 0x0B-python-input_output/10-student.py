#!/usr/bin/python3
"""student class"""


class Student:
    """
        defines a student by: (based on 9-student.py)
    """
    def __init__(self, first_name, last_name, age):
        """
            Initializes instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieves the dictionary
        """
        dictionary = self.__dict__
        if attrs is None:
            return dictionary

        d = {k: v for k, v in dictionary.items() if k in attrs}
        return d
