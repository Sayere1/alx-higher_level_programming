#!/usr/bin/python3

"""function that prints x elements of a list
my_list(List): Element is printed from this list
x(int): num of element
Return: num of element
"""

def safe_print_list(my_list=[], x=0):
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
