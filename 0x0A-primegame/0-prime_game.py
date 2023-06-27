#!/usr/bin/env python3
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
    win = False
    n_list = list(range(2, n + 1))
    for num in n_list:
        # If number of rounds has been completed, exit loop
        if x <= 0:
            break
        # Find the first prime number in the set
        if not isPrime(num):
            continue
        # Delete all multiples of the prime number
        n_list = filter(lambda a: a % num != 0, n_list)
        # Prepare for next loop
        x -= 1
        win = not win

    return win


def isWinner(x, nums):
    """ Predict the winner between Maria and Ben
    Return:
      - Name of the player that wins
    """
    # Handle wrong input
    if x < 0 or len(nums) < 1:
        return None

    # Loop to decide winner
    maria = 0
    ben = 0

    for n in nums:
        if round_x_n(x, n):
            maria += 1
        else:
            ben += 1

    # Decide winner based on boolean
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
