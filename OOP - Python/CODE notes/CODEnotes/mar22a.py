"""
This module illustrates the use of private attributes.
"""

class A:
    def __init__(self, init_a, init_b):
        self.__a = init_a
        self.__b = init_b
    def __str__(self):
        return str(self.__a) + "," + str(self.__b)
