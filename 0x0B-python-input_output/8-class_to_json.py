#!/usr/bin/python3
"""function that defines a Python class-to-JSON.
attributes:
    Class are serializable: list, dict, strng, int
    """


def class_to_json(obj):
    """Return dictionary rep of simple data structure."""
    return obj.__dict__
