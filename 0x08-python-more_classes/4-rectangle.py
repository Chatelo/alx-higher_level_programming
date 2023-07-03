#!/usr/bin/python3
"""
Module 4-rectangle.py
Defines a Rectangle class.
"""


class Rectangle:
    """ Defines a rectangle with attributes width and height. """

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle instance.

        Args:
            width (int): Width of rectangle.
            height (int): Height of rectangle.

        Returns:
            None.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle.

        Args:
            value (int): Width value.

        Returns:
            None.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieves the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle.

        Args:
            value (int): Height value.

        Returns:
            None.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Computes the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Computes the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns string representation of rectangle.

        Returns:
            String representation of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = []
            for i in range(self.__height):
                rect.append("#" * self.__width)
            return "\n".join(rect)

    def __repr__(self):
        """ Returns the representation of the rectangle.

        Returns:
            The representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
