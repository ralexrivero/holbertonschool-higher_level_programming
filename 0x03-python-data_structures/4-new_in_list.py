def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list_cp = my_list.copy()
        my_list_cp[idx] = element
        return my_list_cp
