#!/usr/bin/python3

# prints a dictionary by ordered keys
# Args: dictionar

def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(x, a_dictionary[x])) for x in sorted(a_dictionary)]
