#!/usr/bin/python3
"""func that defien text file-reading."""


def read_file(filename=""):
    """Print UTF8 text file content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
