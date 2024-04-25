#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize the row with 1s
        for j in range(1, i):  # Calculate values inside the row (excluding edges)
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
