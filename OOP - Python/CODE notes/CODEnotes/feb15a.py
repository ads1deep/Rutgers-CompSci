"""
Recursive functions written in class
Author: Suneeta Ramaswami
"""

def list_sum(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + list_sum(L[1:])

def list_min(L):
    if len(L) == 1:
        return L[0]
    else:
        m = list_min(L[1:])
        if m < L[0]:
            return m
        else:
            return L[0]

def reverse_str(astr):
    if len(astr) == 0:
        return ""
    else:
        return reverse_str(astr[1:]) + astr[0]

def palindrome(astr):
    if len(astr) == 0:
        return True
    elif astr[0] != astr[-1]:
        return False
    else:
        return palindrome(astr[1:len(astr)-1])

