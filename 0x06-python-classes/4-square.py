#!/usr/bin/python3

"""A simple example demonstrating the definition of a Square class."""


class Square:
    """A class to represent a square."""

    def __init__(self, size=0):
        """Parameters:
            size (int): The size of the square. Default is 0."""
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
