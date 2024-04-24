# Project Name: 2D Matrix Rotation

This project aims to implement a Python function that rotates a 2D matrix 90 degrees clockwise. The rotation is performed in-place, meaning the original matrix is modified without creating a new one.

## Requirements

To run the project, ensure you have the following:

- Python 3 (version 3.8.10) installed on your system.
- An editor of your choice: vi, vim, or emacs.

## Getting Started

Follow the steps below to set up and run the project:

1. Clone the project repository from [GitHub](https://github.com/your-username/2d-matrix-rotation) or download the source code files.

2. Open a terminal and navigate to the project directory.

3. Run the `main.py` script using the command: `python3 main.py`

4. The rotated matrix will be displayed in the terminal.

## Code Structure

The project consists of the following files:

- `main.py`: The entry point of the project. It demonstrates the usage of the `rotate_2d_matrix` function with a sample matrix.

- `rotate_2d_matrix.py`: Contains the implementation of the `rotate_2d_matrix` function, which rotates a 2D matrix 90 degrees clockwise.

## Usage

To use the `rotate_2d_matrix` function in your own code, follow these steps:

1. Import the function into your Python script: `from rotate_2d_matrix import rotate_2d_matrix`

2. Create a 2D matrix that you want to rotate.

3. Call the `rotate_2d_matrix` function, passing the matrix as an argument: `rotate_2d_matrix(matrix)`

4. The original matrix will be modified and rotated 90 degrees clockwise.

## Example

Here's an example of how to use the `rotate_2d_matrix` function:

```python
from rotate_2d_matrix import rotate_2d_matrix

# Create a sample matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Rotate the matrix
rotate_2d_matrix(matrix)

# Display the rotated matrix
print(matrix)
```

The output will be:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Contributing

Contributions to the project are welcome. If you find any issues or have suggestions for improvements, please submit a pull request or open an issue in the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to your needs.

## Acknowledgements

- The project was inspired by the need to rotate 2D matrices efficiently.
- Thanks to the contributors and developers who have worked on similar projects and shared their knowledge online.
