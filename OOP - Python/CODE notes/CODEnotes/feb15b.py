"""
Recursive function for binary search
Written in class on February 15

Author: Suneeta Ramaswami
"""

def binary_search(L, k):
    if len(L) == 0:
        return False
    else:
        mid = len(L)//2
        if k == L[mid]:
            return True
        elif k < L[mid]:
            return binary_search(L[:mid], k)
        else:
            return binary_search(L[mid+1:], k)

