#!/usr/bin/python3

class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string describing the square.
        """
        return f"Square with size: {self.__size}"
