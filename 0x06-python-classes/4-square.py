#!/usr/bin/python3
"""
Module that contains the Square class
"""


class Square:
    """
    A simple Square class
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
