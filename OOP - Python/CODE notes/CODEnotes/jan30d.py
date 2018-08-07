"""
Author: Suneeta Ramaswami

This module illustrates list comprehension.
"""

def primes(n):
    """
    Return the sorted list of all primes less than or equal to n

    n: a positive integer >= 2
    """
    numbers = list(range(2,n+1))
    result = []
    while len(numbers)>0:
        # remove the zeroth element and its multiples
        p = numbers.pop(0)
        result.append(p)
        numbers = [i for i in numbers if i%p != 0]
    return result


