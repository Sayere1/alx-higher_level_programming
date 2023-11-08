#!/usr/bin/python3

# Args: my_list, tuple: score and weight
# Return: 0

def weight_average(my_list=[]):
    if not my_list:
        return 0
    n_m = 0
    d_n = 0
    for t_p in my_list:
        n_m += t_p[0] * t_p[1]
        d_n += t_p[1]
    return (n_m / d_n)
