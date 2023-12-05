#!/usr/bin/python3
"""class that defines a class Student."""


class Student:
    """Rep a student."""

    def __init__(self, first_name, last_name, age):
        """new Student initialized.
        Args:
            first_name % last_name (str): first name % last name student.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
