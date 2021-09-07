#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"\
          .format(number, number))
elif number == 0:
    print("Las digit of {:d} is 0".format(number))
else:
    print("Last digit of {:d} is {:d} and is less than y and not 0"\
          .format(number, number))
