#!/usr/bin/python3
# prints x elements of a list
def safe_print_list(my_list=[], x=0):
    items = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            items += 1
    except IndexError:
        pass
    print()
    return items
