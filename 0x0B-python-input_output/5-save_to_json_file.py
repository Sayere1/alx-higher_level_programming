#!/usr/bin/python3
"""function that defines a JSON file-writing.
arg: my_obj: python obj
file: file name
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
