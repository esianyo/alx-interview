#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to reach an amount total
    """

    if total < 0:
        return (0)

    dynamicProg = [float('inf')] * (total + 1)
    dynamicProg[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin > amount:
                pass
            elif coin <= amount:
                dynamicProg[amount] = min(dynamicProg[amount],
                                          dynamicProg[amount - coin] + 1)

    return dynamicProg[total] if dynamicProg[total] != float('inf') else -1
