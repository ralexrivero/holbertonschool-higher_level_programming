#!/usr/bin/python3
"""JSON handling"""
import json


def to_json_string(my_obj):
    """
    Returns: the JSON representation of an object (string)
    """
    serialized_json = json.dumps(my_obj)
    return serialized_json
