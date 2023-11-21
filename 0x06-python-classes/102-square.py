#!/usr/bin/python3
"""func that define a class Square."""


class Square:
    """func that represent a square."""

    def __init__(self, size=0):
        """new square.

        Args:
            size (int): new square size.
        """
        self.size = size

    @property
    def size(self):
        """Get or set square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """func that return square area."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == Square comperator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != Square comperator."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < Square comperator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= Square comperator."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > Square comperator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= Square comperator."""
        return self.area() >= other.area()
