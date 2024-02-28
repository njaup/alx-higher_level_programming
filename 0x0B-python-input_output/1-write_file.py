#!/usr/bin/python3
"""Defines a text file-reading function."""


def write_file(filename="", text=""):
    """Writes the given text to a file specified by filename.

    If the file does not exist, it will be created.
    If the file already exists, its content will be overwritten.

    Args:
    filename (str): The name of the file to write to.
    text (str): The text to write to the file.

    Returns:
    int: The number of characters written to the file."""
    num_characters = len(text)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return num_characters
