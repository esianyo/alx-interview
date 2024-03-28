#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the minimum number of copy
    and paste operations needed to reach n characters.

    Args:
        n: The target number of characters.

    Returns:
        The minimum number of operations, or 0 if n is not achievable.
    """

    operations = 0
    curr_len = 1  # Start with 1 character

    while curr_len < n:
        # Find largest power of 2 less than or equal to difference
        diff = n - curr_len
        largest_power_of_2 = 1
        while largest_power_of_2 * 2 <= diff:
            largest_power_of_2 *= 2

        # Increment operations, paste, and update current length
        operations += 1
        curr_len += largest_power_of_2

    return operations
