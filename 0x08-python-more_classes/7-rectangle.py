#!/usr/bin/python3
"""module that define a rectangle class"""


class Rectangle:
    """represent a rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """new Rectangle initialization"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set rectangle width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setting of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set rectangle height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setting the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return rectangle perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """the printable version"""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        final = []
        for i in range(self.__height):
            [final.append(Rectangle.print_symbol) for j in range(self.__width)]
            if i != (self.__height - 1):
                final.append('\n')
        return ("".join(final))

    def __repr__(self):
        """return rectangle string"""
        final = "Rectangle(" + str(self.__width)
        final += ", " + str(self.__height) + ")"
        return (final)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
