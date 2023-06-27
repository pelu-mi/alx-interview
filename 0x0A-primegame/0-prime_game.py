#!/usr/bin/python3
""" Module to implement function for prime game
"""


def isPrime(num: int) -> bool:
    """ Check if number is a prime number
    Returns:
      - True or False
    """
    if num <= 1:
        return False
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            return False
    else:
        return True


def round_x_n(x: int, n: int) -> bool:
    """ Execute each round and return true or false
    Returns:
      - True if Maria wins
      - False if Ben wins
    """
    n_list = list(range(2, n + 1))
    # Reduce list to prime numbers only
    n_list = list(filter(lambda a: isPrime(a), n_list))
    if len(n_list) < x:
        x = len(n_list)
    return False if x % 2 == 0 else True


"""
    if x % 2 == 0:
        return False
    else:
        return True
    """


def isWinner(x, nums):
    """ Predict the winner between Maria and Ben
    Return:
      - Name of the player that wins
    """
    # Handle wrong input
    if x < 1 or not nums:
        return None
    if x != len(nums):
        return None

    # Loop to decide winner
    maria = 0
    ben = 0

    for n in nums:
        if round_x_n(x, n):
            maria += 1
        else:
            ben += 1

    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'
