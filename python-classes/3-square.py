#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute,
size validation, and a method to compute the area.
"""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square, must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
