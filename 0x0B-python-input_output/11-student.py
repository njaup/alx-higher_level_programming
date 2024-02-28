#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Defines a student with first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        """Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Args:
            attrs (list, optional): A list of strings specifying which attributes to include. 
                If None, all attributes are included. Defaults to None.

        Returns:
            dict: A dictionary containing the specified attributes and their values."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Args:
            json (dict): A dictionary containing attribute names and their corresponding values.
                A dictionary key represents the public attribute name, and the corresponding value represents the value of the attribute."""
        for key, value in json.items():
            setattr(self, key, value)
