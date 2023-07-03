#!/usr/bin/python3
"""
This module defines a class 'Rectangle' that
defines a rectangle based on '2-rectangle.py'
"""


class Rectangle:
    """
    Rectangle - Defines a rectangle

    Attributes:
    width (int): width of the rectangle
    height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width - Getter for private attribute width.

        Returns:
        The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width - Setter for private attribute width.

        Args:
        value (int): The value to set the width to

        Raises:
        TypeError: If width is not an integer
        ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height - Getter for private attribute height.

        Returns:
        The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height - Setter for private attribute height.

        Args:
        value (int): The value to set the height to

        Raises:
        TypeError: If height is not an integer
        ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        area - calculates the area of the rectangle

        Returns:
        The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        perimeter - calculates the perimeter of the rectangle

        Returns:
        The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        __str__ - Prints the rectangle using the '#' character.

        Returns:
        str: A string representing the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for i in range(self.height):
            string += "#" * self.width
            if i != self.height - 1:
                string += "\n"
        return string
