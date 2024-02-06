#!/usr/bin/python3

"""A simple example demonstrating the definition of a Square class."""


class Square:
    """A class to represent a square."""

    def __init__(self, size):
        """Args:
            size (int): The size of the square."""
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square."""
        return f"Square with size: {self.__size}"
