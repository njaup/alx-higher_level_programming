#!/usr/bin/python3

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)
