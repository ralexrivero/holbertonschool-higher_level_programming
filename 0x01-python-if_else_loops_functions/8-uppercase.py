#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        print("{0:c}".format(j - 32 if 97 <= j <= 122 else j), end="")
    print("")
