#!/usr/bin/python3
"""Module to find the max integer in a list"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None."""
    if len(list) == 0:
        return None
    data = list[0]
    count = 1
    while count < len(list):
        if list[count] > data:
            data = list[count]
        count += 1
    return data
