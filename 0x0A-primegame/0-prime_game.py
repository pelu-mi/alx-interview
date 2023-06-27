#!/usr/bin/python3
""" Module to implement function for prime game
"""


def rm_multiples(n_list: list, i: int) -> None:
    """ Change values of multiples i in n_list to 0
    """
    for n in range(2, len(n_list)):
        try:
            n_list[n * i] = 0
        except (ValueError, IndexError):
            break


def isWinner(x, nums):
    """ Predict the winner between Maria and Ben
    Return:
      - Name of the player that wins
    """
    # Handle wrong input
    if x < 1 or not nums:
        return None

    maria, ben = 0, 0

    isPrime = [1 for x in range(sorted(nums)[-1] + 1)]
    isPrime[0], isPrime[1] = 0, 0
    for i in range(2, len(isPrime)):
        rm_multiples(isPrime, i)

    for i in nums:
        if sum(isPrime[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Return output
    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'
