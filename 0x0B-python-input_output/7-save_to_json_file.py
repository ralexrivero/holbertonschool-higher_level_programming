#!/usr/bin/python3
"""save_to_json_file function documentation"""

import json


def save_to_json_file(my_obj, filename):
    """adds all arguments to a Python list,
        and then save them to a file
    Args:
        my_obj (class object): object to convert to JSON
        filename (str): output file
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
