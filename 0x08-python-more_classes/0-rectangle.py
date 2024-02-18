#!/usr/bin/python3

class Rectangle:
    def __init__(self, leng, wid):
        self.leng = leng
        self.wid = wid

    def area(self):
        return self.leng * self.wid

    def perimeter(self):
        return 2 * (self.leng + self.wid)

    def is_square(self):
        return self.leng == self.wid
