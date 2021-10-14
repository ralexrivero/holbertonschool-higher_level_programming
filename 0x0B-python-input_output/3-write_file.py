#!/usr/bin/python3
"""write_file function documentation"""


def write_file(filename="", text=""):
    """returns the JSON representation of an object (string)
    Args:
        filename (str): input file
        text (str): text to write into file
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        written = f.write(text)
    return written
