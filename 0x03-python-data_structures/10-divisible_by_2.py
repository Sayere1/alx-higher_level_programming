#!/usr/bin/python3

# Args: my_list, return: nw_list
def divisible_by_2(my_list=[]):
    nw_list = []
    for i in my_list:
        nw_list.append(i % 2 == 0)
    return (nw_list)
