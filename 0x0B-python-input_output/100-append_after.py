#!/usr/bin/python3
"""function that defines a text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """text are inserted after each line
    note: these lines contain a given string in a file.

    Args:
        filename % search_string(str): name % string in the file.
        note: the search_string can be located in the file.
        new_string (str): inserted string.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
