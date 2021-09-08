#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        j = i
    else:
        j = i - 32
    print("{0:c}".format(j), end="")
