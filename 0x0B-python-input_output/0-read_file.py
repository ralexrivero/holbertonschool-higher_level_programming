#!/usr/bin/python3
"""read_file function documentation """


def read_file(filename=""):
    """Function that reads the file and prints its contents to stdout
    Args:
        filename (str): filename to open
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
