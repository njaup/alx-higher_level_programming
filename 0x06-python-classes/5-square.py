#!/usr/bin/python3

"""A simple example demonstrating the definition of a Square class."""


class Square:
    """A class to represent a square."""

    def __init__(self, size=0):
        """Parameters:
        size (int): The size of the square (default 0)."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Prints the square using the '#' character.

        If the size of the square is 0, prints an empty line."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
