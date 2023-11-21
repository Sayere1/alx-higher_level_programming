#!/usr/bin/python3
"""module that efine a class Square."""


class Square:
    """module that epresent a square."""

    def __init__(self, size):
        """new square initialized.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set square current size."""
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

    def my_print(self):
        """Print # characterfrom the square."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
