#!/usr/bin/python3
"""
Prime Game that calculate the winner base on the prime
number choose in the given set of numbers.
"""


def prime(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Method that determine the winner of a prime number

    Args:
        xi: s the nuber of rounds
        nums: is an array of n

    Return:
        return name of the player that won the most rounds
    """

    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria, Ben = 0, 0

    for i in range(x):
        primes = prime(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    # Determine the overall winner
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
