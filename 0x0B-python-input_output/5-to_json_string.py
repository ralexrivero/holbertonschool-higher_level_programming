#!/usr/bin/python3
"""to_json_string function documentation"""


import json


def to_json_string(my_obj):
    """
    writes an Object to a text file, using a JSON representation
    Args:
        my_obj (class object):  object to converto to JSON
    Returns:
        JSON string
    """

    return json.dumps(my_obj)
