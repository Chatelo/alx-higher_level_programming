#!/usr/bin/python3


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        list: Result of multiplying the matrices.

    Raises:
        TypeError: If m_a or m_b is not a list of lists or if one element of those
            list of lists is not an integer or a float.
        ValueError: If m_a or m_b is empty (it means: = [] or = [[]]) or if m_a
            and m_b can't be multiplied.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    try:
        result = np.dot(np.array(m_a), np.array(m_b)).tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

    return result
