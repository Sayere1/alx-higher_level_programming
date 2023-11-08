#!/usr/bin/python3

# Add all unique integers
# Args: my_list , Return: sum

def uniq_add(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return (0)
    uniq = sorted(set(my_list))
    return (sum(uniq))
