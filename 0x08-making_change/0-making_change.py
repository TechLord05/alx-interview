#!/usr/bin/python3
"""Making change algorithm"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    makeChange is a method that determine the fewest number
    of coins needed to meet a given amount total.

    Args:
        - coins[int]: list of coins to make change
        - total(int): total amount given
    Returns:
        return fewest number of coins needed to meet total
    Algorithm Used:
        Greedy algorithm
    """

    if total <= 0:
        return 0

    amount = total
    coins_count = 0
    coin_indx = 0
    coins_len = len(coins)
    sorted_coins = sorted(coins, reverse=True)

    while amount > 0:
        if coin_indx >= coins_len:
            return -1
        if amount - sorted_coins[coin_indx] >= 0:
            amount -= sorted_coins[coin_indx]
            coins_count += 1
        else:
            coin_indx += 1
    return coins_count
