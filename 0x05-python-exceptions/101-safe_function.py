#!/usr/bin/python3

# executes a function safely.

from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result
