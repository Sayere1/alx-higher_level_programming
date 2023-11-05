#!/usr/bin/python3

def element_at(my_list, idx):
    """Args:
        my-list: the list
        idx: the index

    Returns: None if idx is -, out of range idex value is found
    """

    if (idx < 0 or idx > (len(my_list) - 1)):
        return (None)
    return (my_list[idx])
