#!/usr/bin/python3
"""function that defines a string-to-JSON."""
import json


def to_json_string(my_obj):
    """Return JSON representation of a strng object."""
    return json.dumps(my_obj)
