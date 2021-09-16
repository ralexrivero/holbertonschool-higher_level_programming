#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0
    return sum(s * w for s, w in my_list) / sum(w for s, w in my_list)
