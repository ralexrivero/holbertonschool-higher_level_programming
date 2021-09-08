#!/usr/bin/python3
letter = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print('{}'.format(chr(i - letter)), end='')
    letter = 32 if letter == 0 else 0
