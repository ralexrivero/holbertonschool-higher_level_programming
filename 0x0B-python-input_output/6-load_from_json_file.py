#!/usr/bin/python3
"""creates an object"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file
    """
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
    return data
