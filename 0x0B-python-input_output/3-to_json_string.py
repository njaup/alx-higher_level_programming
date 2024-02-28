#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Parameters:
        my_obj (object): The object to be serialized to JSON.

    Returns:
        str: JSON representation of the object."""
    return json.dumps(my_obj)
