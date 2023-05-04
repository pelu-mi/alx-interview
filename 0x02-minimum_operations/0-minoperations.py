#!/usr/bin/python3
""" Minimum Operations
"""


import sys


def minOperations(n):
    """ Return minimum operations required to generate n characters
    """
    if (n < 1) or not isinstance(n, int):
        return 0
    # Test
    ops = 0
    copied = 0
    done = 1
    while done < n:
        if copied == 0:
            # First operation: copy all and paste
            copied = done
            done += copied
            ops += 2
        elif n - done > 0 and (n - done) % done == 0:
            # Copy all and paste
            copied = done
            done += copied
            ops += 2
        elif copied > 0:
            # Paste only
            done += copied
            ops += 1
    return ops
