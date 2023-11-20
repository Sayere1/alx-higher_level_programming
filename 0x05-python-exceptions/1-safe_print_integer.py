#!/usr/bin/python3

# Args: value (int)
# Return: false if any error occur otw true

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
