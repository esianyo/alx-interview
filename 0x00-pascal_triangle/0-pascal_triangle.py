#!/usr/bin/python3
"""that returns a list of intergers representing the Pascals triangle"""


def pascal_triangle(n):
    """function that returns integers that draw a triangle"""
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        new_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                new_list.append(1)
            else:
                new_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(new_list)

    return triangle
