#!/usr/bin/python3
"""class_to_json function documentation"""


def class_to_json(obj):
    """Returns a dictionary of an object (JSON)
    Args:
        obj (class object): object to serialize
    """

    return obj.__dict__
