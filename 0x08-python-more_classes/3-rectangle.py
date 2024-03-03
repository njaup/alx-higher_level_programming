#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Represent the rectangle as a string of '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            rectangle += "#" * self.width
            if i < self.height - 1:
                rectangle += "\n"
        return rectangle
