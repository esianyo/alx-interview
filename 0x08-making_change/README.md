# Project: Making Change

This project implements a Python function `makeChange` that calculates the fewest number of coins needed to meet a given amount total. The function takes a list of coin values and a target total as parameters.

## Requirements

To run the project, ensure you have the following:

- Python 3 (version 3.4.3) installed on your system.
- An editor of your choice: vi, vim, or emacs.

## Getting Started

Follow the steps below to set up and run the project:

1. Clone the project repository from [GitHub](https://github.com/your-username/making-change) or download the source code files.

2. Open a terminal and navigate to the project directory.

3. Run the `0-making_change.py` script using the command: `./0-making_change.py`

4. The output will display the fewest number of coins needed to meet the target total for the provided test cases.

## Code Explanation

The project consists of the following file:

- `0-making_change.py`: Contains the implementation of the `makeChange` function, which calculates the fewest number of coins needed to meet a given amount total.

The `makeChange` function works as follows:

1. Initializes a dynamic programming array `dp` with a length of `total + 1`, where `total` is the target amount. Each element is set to infinity.

2. Sets `dp[0] = 0` to indicate that zero coins are needed to reach an amount of zero.

3. Iterates from `1` to `total`, and for each amount `i`, iterates through each coin value in the `coins` list.

4. If the current coin value is less than or equal to the current amount, updates `dp[i]` to be the minimum of its current value and `dp[i - coin] + 1`. This represents the minimum number of coins needed to reach the current amount.

5. After the iteration, `dp[total]` will contain the fewest number of coins needed to reach the target total. If it is still infinity, the total cannot be met by the available coins, so `-1` is returned. Otherwise, `dp[total]` is returned.

## Usage

To use the `makeChange` function in your own code, follow these steps:

1. Import the function into your Python script: `from 0-making_change import makeChange`

2. Create a list of coin values and a target total.

3. Call the `makeChange` function, passing the coin values and target total as arguments: `makeChange(coins, total)`

4. The function will return the fewest number of coins needed to meet the target total.

## Example

Here's an example of how to use the `makeChange` function:

```python
from 0-making_change import makeChange

coins = [1, 2, 25]
total = 37

result = makeChange(coins, total)
print(result)  # Output: 7
```

In this example, the `makeChange` function is called with a list of coin values `[1, 2, 25]` and a target total of `37`. It calculates that the fewest number of coins needed to meet the target total is `7`, and the result is printed.

## Additional Notes

- If the target total cannot be met by any combination of the available coins, the function will return `-1`.
- The function assumes that the list of coin values contains positive integers greater than 0.
