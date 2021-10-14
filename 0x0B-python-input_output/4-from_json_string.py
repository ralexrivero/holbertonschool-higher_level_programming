#!/usr/bin/python3
"""JSON handling"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)
        represented by a JSON string"""
    deserialized_json = json.loads(my_str)
    return deserialized_json
