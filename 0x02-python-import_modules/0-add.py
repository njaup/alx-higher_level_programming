#!/usr/bin/python3
def add(a, b):
    return a + b

a = 1
b = 2
from add_0 import add
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
