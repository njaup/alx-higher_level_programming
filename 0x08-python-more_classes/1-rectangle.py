#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, data):
        if not isinstance(data, int):
            raise TypeError("width must be an integer")
        elif data < 0:
            raise valueError("width must be >= 0")
        else:
            self.__width = data

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, data):
        if not isinstance(data, int):
            raise TypeError("height must be an integer")
        elif data < 0:
            raise valueError("height must be >= 0")
        else:
            self.__height = data
