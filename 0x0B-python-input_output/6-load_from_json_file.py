#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Load data from a JSON file and return the corresponding Python object.

    Args:
        filename (str): The path to the JSON file to be loaded.

    Returns:
        obj: The Python object representing the data loaded from the JSON file."""
    with open(filename, "r") as file:
        data = json.load(file)
    return data
