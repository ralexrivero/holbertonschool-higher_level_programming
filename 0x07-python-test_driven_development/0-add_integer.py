#!/usr/bin/python3
""" adds 2 integers """


def add_integer(a, b=98):
    """
        adds two integers
        Args:
            a (int): first value
            b (int, optional): second value
        Returns:
            adition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        b = int(b)
    res = a + b
    return res
