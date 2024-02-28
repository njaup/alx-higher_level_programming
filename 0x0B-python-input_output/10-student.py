#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student object.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.

        If attrs is provided, only the specified attributes are included.
        Otherwise, all attributes are included.

        Parameters:
        - attrs (list of str): List of attribute names to include. Defaults to None.

        Returns:
        - dict: A dictionary containing attribute names and values."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
