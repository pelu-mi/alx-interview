#!/usr/bin/python3
""" Module for alx interview 4
"""


def validUTF8(data):
    """ Method to check for valid utf8 expressions
    """
    count = 0
    for x in data:
        while x > 256:
            x -= 256
        if count == 0:
            if x >> 5 == 0b110:  # Check if the msbs are 110
                count = 1
            elif x >> 4 == 0b1110:  # Check if the msbs are 1110
                count = 2
            elif x >> 3 == 0b11110:  # Check if the msbs are 11110
                count = 3
            elif x >> 7 != 0:  # Check if the number starts with 1
                return False
        else:
            if x >> 6 != 0b10:  # Chek if the continuation byte starts with 10
                return False
            count = count - 1  # If it does, move to the next byte
    return (count == 0)  # Check if there are no missing continuation bytes
