#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Args:
        filename (str): The name of the file to read. Default is an empty string.

    Returns:
        None

    Note:
        If the file is not found, it prints an appropriate message."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
