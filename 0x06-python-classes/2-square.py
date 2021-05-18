#!/usr/bin/python3
"""Square class defined by size and"""


class Square:
    """Inside the class yeahhh"""

    def __init__(self, size=0):
        """Functon to do everything"""
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
