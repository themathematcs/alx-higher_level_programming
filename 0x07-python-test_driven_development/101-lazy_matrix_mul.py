#!/usr/bin/python3
"""
lazy_matrix module
This function calculates multiplication of matrix using numpy lib
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return: a nex matrix with the product of m_a and m_b
    Args:
    param1: m_a type list of list is a matrix
    param2: m_b type list of list is a matrix
    Raise: TypeError, ValueError
    """
    return (np.matmul(m_a, m_b))
