#!/usr/bin/python3
def no_c(my_string):

    """Arg: my_string: the string
    Return: n_string
    """

    n_string = my_string.translate({ord(i): None for i in 'cC'})
    return n_string
