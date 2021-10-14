#!/usr/bin/python3
"""append_write function documentation"""


def append_write(filename="", text=""):
    """returns an object (Python data structure)
        represented by a JSON string
    Args:
        filename (str): input file
        text (str): text to append into file
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        written = f.write(text)
    return written
