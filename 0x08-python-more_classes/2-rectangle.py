#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of the Rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Returns the height of the Rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of the Rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle instance
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
