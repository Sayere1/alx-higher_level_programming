#!/usr/bin/python3
"""Defines a specific class function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any) % a_class (type)
    Returns: true If obj is exactly an instance of a_class.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
