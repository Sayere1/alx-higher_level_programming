#!/usr/bin/python3
"""inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): object to check % a_class (type): class to match.
    Returns: True if obj is instance or inherited otw false
    """
    if isinstance(obj, a_class):
        return True
    return False
