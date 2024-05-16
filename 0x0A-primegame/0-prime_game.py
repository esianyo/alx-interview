#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the prime game for multiple rounds.

    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n,
    they take turns choosing a prime number from the set
    and removing that number and its multiples from the set.
    The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and
    both players play optimally, determine who the winner of each game is.

    Args:
        x (int): Number of rounds.
        nums (List[int]): List of n values for each round.

    Returns:
        str: Name of the player that won the most rounds ("Maria" or "Ben").
             Returns None if the winner cannot be determined.

    Raises:
        ValueError: If the input grid is not a valid 2D list of booleans.
    """
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to create the sieve
    max_num = max(nums)

    # Sieve of Eratosthenes to find all prime numbers up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    p = 2
    while p * p <= max_num:
        if sieve[p]:
            for i in range(p * p, max_num + 1, p):
                sieve[i] = False
        p += 1

    # List of primes up to max_num
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]

    def play_round(n):
        """
        Simulates a single round of the game for a given n.

        Args:
            n (int): The end number for the round (1 to n).

        Returns:
            int: 0 if Maria wins, 1 if Ben wins.
        """
        remaining = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while True:
            # Find the smallest prime in the remaining numbers
            move_made = False
            for prime in primes:
                if prime in remaining:
                    # Maria or Ben picks the prime and removes its multiples
                    multiples = set(range(prime, n + 1, prime))
                    remaining -= multiples
                    move_made = True
                    break

            if not move_made:
                # If no move was made, the current player loses
                return 1 - turn

            turn = 1 - turn  # Switch turns

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = play_round(n)
            if winner == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
