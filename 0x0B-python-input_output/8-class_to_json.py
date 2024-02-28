#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Convert an object into a dictionary containing only serializable data types.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of the object with serializable attributes.
    """
    if isinstance(obj, (str, int, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        return {key: class_to_json(value) for key, value in obj.__dict__.items() if class_to_json(value) is not None}
    else:
        return None
