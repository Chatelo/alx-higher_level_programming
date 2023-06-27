#!/usr/bin/python3
"""This module defines a class MagicClass."""

import math


class MagicClass:
    """A class MagicClass that represents a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass instance with a given radius."""
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """Return the area of the circle."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
