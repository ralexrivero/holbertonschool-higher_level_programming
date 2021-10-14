#!/usr/bin/python3
"""number_of_lines function documentation"""


def number_of_lines(filename=""):
    """writes a string to a text file (UTF8)
        and returns the number of characters written
    Args:
        filename (str): input filename
    Returns:
        number of lines
    """

    lines = 0
    with open(filename, encoding='utf-8') as f:
        for i in f:
            lines += 1
        return lines
