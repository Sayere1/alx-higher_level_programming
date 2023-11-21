#!/usr/bin/python3
"""module that define a class Square."""


class Square:
    """module that represent a square."""

    def __init__(self, size=0):
        """new square initialized.

        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return current square."""
        return (self.__size * self.__size)
