#!/usr/bin/python3
"""func that defines a file-writing."""


def write_file(filename="", text=""):
    """Write UTF8 text file string.

    Args:
        filename % text(str): The file name and text to write.
    Returns: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
