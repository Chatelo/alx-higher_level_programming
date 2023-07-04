#!/usr/bin/python3
"""Module for saying my name."""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    :param first_name: First name
    :param last_name: Last name (optional)
    :type first_name: str
    :type last_name: str
    :raises TypeError: If either of the arguments is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
