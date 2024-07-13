#!/usr/bin/python3

"""
 pascal_triangle
"""


def fact(n):
    """
    Returns the factorial of n
    """
    if n < 0:
        return None  # or raise an exception
    elif n == 0:
        return 1
    else:
        return n * fact(n - 1)


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(fact(i) // (fact(j) * fact(i - j)))
        triangle.append(row)
    return triangle
