#!/usr/bin/python3
"""module that define a class Square."""


class Square:
    """module that represent a square."""

    def __init__(self, size=0):
        """new square initialized.
        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the square current size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square current area."""
        return (self.__size * self.__size)
