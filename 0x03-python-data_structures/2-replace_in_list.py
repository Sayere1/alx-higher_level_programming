#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Args:
        my_list: the list, idx: the index
        element: the element to be placed at the index

    Returns: null
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list)
    my_list[idx] = element
    return (my_list)
