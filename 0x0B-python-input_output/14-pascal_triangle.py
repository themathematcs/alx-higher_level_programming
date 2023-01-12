#!/usr/bin/python3
"""
    Technical interview preparation:
    You are not allowed to google anything
    Whiteboard first
    Create a function def pascal_triangle(n): that
    returns a list of lists of integers representing
    the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""


def pascal_triangle(n):
    """ makes a list of lists representing a pascal tringle """
    lista = []
    if n <= 0:
        return lista
    if n >= 1:
        lista.append([1])
    for i in range(1, n):
        lista.append([1])
        for j in range(len(lista[i - 1]) - 1):
            lista[i].append(lista[i - 1][j] + lista[i - 1][j + 1])
        lista[i].append(1)
    return lista
