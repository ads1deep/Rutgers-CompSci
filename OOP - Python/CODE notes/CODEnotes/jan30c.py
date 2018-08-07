"""
Author: Suneeta Ramaswami

This module contains simple examples of functions
and the use of lists.
"""

import math

def is_prime(n):
    """
    Returns True if a positive integer n is prime and False otherwise

    n: A positive integer
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def list_of_primes(K):
    """
    Returns a list of all primes that are less than or equal to K

    K: A positive integer
    """

    # Uses list comprehension
    # return [i for i in range(2, K+1) if is_prime(i)]

    # Uses filter function
    return list(filter(is_prime, range(2, K+1)))

    # L = []
    # for num in range(2, K+1):
    #    if is_prime(num):
    #        L.append(num)
    # return L

    


