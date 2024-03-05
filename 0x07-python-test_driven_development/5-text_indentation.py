#!/usr/bin/python3
"""Defines a square-printing function."""


def text_indentation(text):
    """Prints the text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text to be processed.
    Raises:
        TypeError: If the input text is not a string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_added = False

    for char in text:
        if not new_line_added and char.strip() != '':
            print(char, end='')
            new_line_added = True
        elif char in ['.', '?', ':']:
            print(char + '\n')
            new_line_added = False
        else:
            print(char, end='')
