#!/usr/bin/python3
"""func that defines a file-appending."""


def append_write(filename="", text=""):
    """a string is appended at the end of UTF8 text file.

    Args:
        filename % text(str): The name % text file to append.
    Returns:number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
