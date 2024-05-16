#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win(primes, n):
        if n in primes:
            return True
        for prime in primes:
            if n % prime == 0:
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        primes = get_primes(nums[i])
        if can_win(primes, nums[i]):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
