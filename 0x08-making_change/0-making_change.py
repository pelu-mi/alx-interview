#!/usr/bin/python3
""" Module to solve Making change problem
"""


def makeChange(coins, total):
    """ Given a list of coins of different values, determine the fewest
        number of coins needed to meet a given amount
    """
    count = 0
    change = 0
    coins.sort(reverse=True)
    coins = list(filter(lambda x: (x <= total), coins))
    for i in range(len(coins)):
        if change >= total:
            continue
        while (change + coins[i] <= total):
            change += coins[i]
            count += 1
    if change == total:
        return (count)
    else:
        return (-1)
