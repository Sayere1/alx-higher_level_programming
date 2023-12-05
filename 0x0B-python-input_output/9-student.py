#!/usr/bin/python3
"""class that defines a class Student."""


class Student:
    """Rep student."""

    def __init__(self, first_name, last_name, age):
        """new Student initialized.
        Args:
            first_name % last_name (str): first name % last name student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dict rep of the Student."""
        return self.__dict__
