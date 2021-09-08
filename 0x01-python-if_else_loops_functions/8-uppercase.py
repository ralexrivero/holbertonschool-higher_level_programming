#!/usr/bin/pyton3
def uppercase(str):
    for i in str:
        j = ord(i)
        print("{0:c}".format(i -32 if ord('a') <= j <= ord('z') else i), end="")
        print()

