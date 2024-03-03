#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Class to represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for _ in range(self.height):
            rect += "#" * self.width + "\n"
        return rect[:-1]

    def __repr__(self):
        """Return a string representation that can recreate the instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Destructor method to print a message when an instance is deleted."""
        print("Bye rectangle...")
