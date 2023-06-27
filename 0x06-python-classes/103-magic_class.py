#!/usr/bin/python3

import math


class MagicClass:

    def __init__(self, radius=0):
        """Initialize a MagicClass instance with a given radius."""
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
