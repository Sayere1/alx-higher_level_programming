#!/usr/bin/python3
"""direct or indirect inherited class-checking function."""


def inherits_from(obj, a_class):
    """define if an object is an inherited instance of a class.

    Args:
        obj (any): object to check % a_class (type): class to match.
    Returns:true if obj is an inherited instance otw false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
