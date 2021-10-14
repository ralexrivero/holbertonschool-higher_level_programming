#!/usr/bin/python3
"""load_from_json_file function documentation"""


import json


def load_from_json_file(filename):
    """returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
    Args:
        filename (str): input file
    Returns:
        the JSON object
    """

    with open(filename) as f:
        json_obj = json.load(f)
    return json_obj
