#!/usr/bin/python3
# args: my_list - contain int
# Return: max
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    minimum_value = -10000000
    for i in my_list:
        if i > minimum_value:
            minimum_value = i
    return (minimum_value)
