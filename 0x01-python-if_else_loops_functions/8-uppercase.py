#!/usr/bin/pyton3
def uppercase(str):
    j = 0
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            j = (ord(i) - 32)
        else:
            j = ord(i)
        print('{0:c}'.format(j), end='')
    print("")
