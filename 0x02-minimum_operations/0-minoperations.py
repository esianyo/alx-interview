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

    if n <= 1:
        return 0

    operations = n

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            operations = min(operations, i + minOperations(n // i))

    return operations


if __name__ == "__main__":
    # Example usage:
    n = 9
    print("Number of operations for", n, "characters:", minOperations(n))
