#!/usr/bin/python3
"""func that define a MagicClass matching a bytecode."""

import math


class MagicClass:
    """func epresenting circle."""

    def __init__(self, radius=0):
        """magicClass initialized.

        Arg:
            radius (float or int): new MagicClass radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return magicClass area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return magicClass circumference."""
        return (2 * math.pi * self.__radius)
