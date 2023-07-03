#!/usr/bin/python3
"""
This module defines a class 'Rectangle' that represents a rectangle
"""


class Rectangle:
    """
    A 'Rectangle' class definition
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of a 'Rectangle' class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the 'width' property

        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the 'width' property

        Args:
            value (int): The value to set the 'width' property to

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value' is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the 'height' property

        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the 'height' property

        Args:
            value (int): The value to set the 'height' property to

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value' is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Computes the area of the rectangle

        Returns:
            The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            A string representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ''
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that
        can be used to recreate it

        Returns:
            A string representation of the rectangle
            that can be used to recreate it
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """
        Deletes an instance of a 'Rectangle' class
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
