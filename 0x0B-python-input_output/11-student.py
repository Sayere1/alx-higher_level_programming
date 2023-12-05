#!/usr/bin/python3
"""class tha defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """new Student initialized.
        Args:
            first_name % last_name(str): first name % last name of student.
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

    def reload_from_json(self, json):
        """Student attributes replaced.
        Args:
            json (dict): The value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
