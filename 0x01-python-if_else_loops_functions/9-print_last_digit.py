#!/usr/bin/python3

def print_last_digit(x):
    if x > 0:
        print (x % 10, end="")
        return (x % 10)
    elif x == 0:
        print(0, end="")
        return (0)
    else:
        print(-x % 10, end="")
        return (-x % 10)
