#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Args:
        my_list: the list, idx: the index, element: to be modify

    Returns: new_list
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list.copy())
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
