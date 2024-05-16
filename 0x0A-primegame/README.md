# Prime Game

Prime Game is a game where two players, Maria and Ben, take turns choosing a prime number and removing that number and its multiples from a set of consecutive integers. The player who cannot make a move loses the game. This project provides a solution to determine the winner of each round of the Prime Game.

## Installation

1. Clone the repository:
   ```
   git clone repo url
   ```

2. Navigate to the project directory:
   ```
   cd prime-game
   ```

3. The project does not require any additional packages or dependencies. It is implemented in Python 3 and follows the PEP 8 style.

## Usage

The main functionality of the Prime Game is implemented in the `isWinner(x, nums)` function, where `x` is the number of rounds and `nums` is an array of integers representing the range for each round.

To use the Prime Game, follow these steps:

1. Import the `isWinner` function from the `prime_game` module:
   ```python
   from prime_game import isWinner
   ```

2. Call the `isWinner` function with the desired number of rounds and the array of integers:
   ```python
   winner = isWinner(5, [2, 5, 1, 4, 3])
   ```

3. The function will return the name of the player who won the most rounds or `None` if the winner cannot be determined.

   Example:
   ```python
   if winner is not None:
       print("Winner: {}".format(winner))
   else:
       print("The winner cannot be determined.")
   ```

   The output will be:
   ```
   Winner: Ben
   ```

## Approach

The solution to the Prime Game problem is based on the following approach:

1. Implement a helper function `is_prime(n)` to check if a number is prime.
2. Implement a helper function `get_primes(n)` to generate a list of prime numbers up to a given limit.
3. Implement a helper function `can_win(primes, n)` to check if a player can win for a given number.
4. Iterate through each round and determine the winner based on the available prime numbers.
5. Count the number of wins for Maria and Ben.
6. Return the name of the player with the most wins or `None` if the winner cannot be determined.

## Limitations

- The solution assumes that the input values `x` and `nums` are within a reasonable range (not larger than 10000) to ensure efficient execution.
- The solution does not import any external packages and relies only on the standard Python library.

## Contributing

Contributions to the Prime Game project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

The Prime Game project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
