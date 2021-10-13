#!/usr/bin/python3
"""class instance checker"""


def is_same_class(obj, a_class):
    """Checks IF object is exactly an instance of the specified class
    Returns:
        True if the object is exactly an instance of the specified clasS
        otherwise False
    """

    if type(obj) == a_class:
        return True
    else:
        return False
