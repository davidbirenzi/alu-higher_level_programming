#!/usr/bin/python3

"""
Module 3-rectangle.py

This module defines the Rectangle class, which represents a rectangle with
private attributes for width and height. It includes getters and setters for
both attributes to enforce type checking and validation, along with methods
to calculate area and perimeter. Additionally, it provides methods to represent
the rectangle as a string for print() and str() functions.

"""

class Rectangle:
    """
    Class representing a rectangle.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a formal string representation of the rectangle.

        """
        return f"<{type(self).__name__} object at {hex(id(self))}>"
