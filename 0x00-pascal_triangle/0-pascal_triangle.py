def pascal_triangle(n):
    """
  Generates Pascal's triangle for a given number of rows (n).

  Args:
      n: The number of rows in the Pascal's triangle.

  Returns:
      A list of lists representing the Pascal's triangle.
      Returns an empty list if n <= 0.
  """

  if n <= 0:
      return []

  triangle = [[1]]  # Start with the first row (always [1])
  for i in range(1, n):
      # Build the next row based on the previous row
    prev_row = triangle[i-1]
    next_row = [1]  # Every row starts with 1
    for j in range(1, i):
        # Add the sum of adjacent elements from the previous row
      next_row.append(prev_row[j-1] + prev_row[j])
    next_row.append(1)  # Every row ends with 1
    triangle.append(next_row)

  return triangle
