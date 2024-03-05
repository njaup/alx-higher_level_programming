#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def validate_matrix(matrix):
    """Validate the input matrix according to specified requirements.
    
    Args:
        matrix (list): The matrix to be validated. 
    Raises:
        TypeError: If the matrix is not a list, not a list of lists,
                   or contains elements other than integers or floats.
        ValueError: If the matrix is empty or rows are of different sizes."""
    if not isinstance(matrix, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not matrix:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not all(isinstance(val, (int, float)) for row in matrix for val in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")


def matrix_mul(m_a, m_b):
    """Perform matrix multiplication of two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.
    Returns:
        list: The resulting matrix after multiplication.
    Raises:
        TypeError: If the matrices are not valid according to requirements.
        ValueError: If the matrices cannot be multiplied."""
    validate_matrix(m_a)
    validate_matrix(m_b)
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]
    
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
