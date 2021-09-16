#!/usr/bin/python3
def complex_delete(a_dictionary, target):
    for key, value in dict(a_dictionary).items():
        if value == target:
            del a_dictionary[key]
    return a_dictionary
