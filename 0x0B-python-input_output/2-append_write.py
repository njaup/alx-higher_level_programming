#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Append the given text to the end of the specified file.

    Args:
        filename (str): The path to the file to which text will be appended.
        text (str): The text to append to the file.

    Returns:
        int:

    Raises:
        Exception: If an error occurs during the file operation."""
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print("An error occurred:", e)
        return 0
