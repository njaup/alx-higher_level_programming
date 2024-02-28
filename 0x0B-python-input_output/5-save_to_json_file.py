#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Serialize the given object to a JSON representation and save it to a file.

    Args:
    my_obj: The object to be serialized.
    filename: The name of the file to save the JSON representation to.

    Returns:
    None"""
        with open(filename, 'w') as file:
            json.dump(my_obj, file)
