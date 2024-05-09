#!/usr/bin/python3

"""
Calculates the perimeter of the island in a 2D grid of integers.

This function takes a 2D list of integers representing the island map
(0 for water, 1 for land) and returns the total perimeter of the island
(sum of exposed sides).

Args:
    grid: A 2D list of integers representing
    the island map (0 for water, 1 for land).

Returns:
    The total perimeter of the island (sum of exposed sides).

Raises:
    ValueError: If the input grid is not a valid 2D list of integers.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the provided grid.

    Args:
        grid: A 2D list of integers representing
        the island map (0 for water, 1 for land).

    Returns:
        The total perimeter of the island (sum of exposed sides).
    """

    # Validate input grid format
    if not isinstance(grid, list) or not all(isinstance(row, list) and all(isinstance(cell, int) for cell in row) for row in grid):
        raise ValueError("Invalid grid format. Grid must be a 2D list of integers.")

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            # Check if current cell is land
            if grid[i][j] == 1:
                # Add perimeter for each side (except if connected to land)
                perimeter += 4

                # Check left neighbor (if within grid bounds)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check top neighbor (if within grid bounds)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter


# Make the function available for import
if __name__ == "__main__":
    pass
