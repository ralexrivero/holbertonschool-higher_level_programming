#!/usr/bin/python3
"""read_lines function documentation"""


def read_lines(filename="", nb_lines=0):
    """appends a string at the end of a text file (UTF8)
        and returns the number of characters added
    Args:
        filename (str): input filename
        nb_lines (int): number of lines to print
    """

    lines = 0
    with open(filename, encoding='utf-8') as f:
        for l in f:
            lines += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= lines:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
