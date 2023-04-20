#!/usr/bin/python3
""" Module for pascal triangle implementation
"""


def pascal_triangle(n):
    """ Simple implementation of pacal triangle
    """
    res = [[1] * i for i in range(1, n + 1)]
    for row in range(2, n):
        for i in range(1, len(res[row]) - 1):
            res[row][i] = res[row - 1][i - 1] + res[row - 1][i]
    return res
