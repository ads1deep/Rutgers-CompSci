"""
This module illustrates the use of private attributes
and private methods.
"""

class A:
    def __init__(self):
        self.__a = 5
    def __str__(self):
        return str(self.__a)
    def __secret(self):
        self.__a *= 2
    def method1(self):
        self.__secret()

