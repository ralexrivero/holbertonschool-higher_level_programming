#!/usr/bin/python3
"""from_json_string documentation"""


import json


def from_json_string(my_str):
    """creates an Object from a “JSON file”:
    Args:
        my_str (seralized str): the string to convert to object
    Returns:
        the deserialized string
    """

    return json.loads(my_str)
