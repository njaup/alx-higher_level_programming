#!/usr/bin/python3

"""A simple example demonstrating the definition of a Square class."""


class Square:
    """A class to represent a square."""

    def __init__(self, size=0):
        """Args:
        size (int, optional): The size of the square. Defaults to 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
