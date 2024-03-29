#!/usr/bin/python3
"""
Contains method that calculates the fewest number of ops
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns the fewest number of ops needed to result in exactly
    n H characters in the file.
    """
    ops = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            ops += min_ops
            n /= min_ops
        min_ops += 1
    return ops
