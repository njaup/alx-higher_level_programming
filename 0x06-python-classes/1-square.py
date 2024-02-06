#!/usr/bin/python3

class Square:
    """A class to represent a square with a given size."""

    def __init__(self, size):
        """Initialize the Square with the given size."""
        self.__size = size

    def __str__(self):
        """Return a string representation of the square."""
        return f"Square with size: {self.__size}"
