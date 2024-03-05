#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int or float): The matrix to be divided.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats or
            if each row of the matrix does not have the same size, or if div
            is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists of float: A new matrix with elements divided by div
            rounded to 2 decimal places."""
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
