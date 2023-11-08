#!/usr/bin/python3

"""
0-square_matrix_simple.py
This module defines the square_matrix_simple function which
computes the square value of all integers of a matrix.
"""

def square_matrix_simple(matrix):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list): A 2 dimensional array.

    Returns:
        list: A new matrix with each value as the square of the value of the input.
    """
    new_matrix = [[num**2 for num in row] for row in matrix]
    return new_matrix
