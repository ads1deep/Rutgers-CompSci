"""
This module implements a class for the stack data structure. 
"""

class Stack:
    def __init__(self):
        self.__slist = []
    def push(self, item):
        self.__slist.append(item)
    def pop(self):
        if not self.empty():
            return self.__slist.pop()
    def size(self):
        return len(self.__slist)
    def empty(self):
        return self.size() == 0
    def top(self):
        if not self.empty():
            return self.__slist[-1]
    
    
