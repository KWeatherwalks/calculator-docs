# calculator/calculations.py

"""Pvoride several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""


from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)


def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0
        >>> subtract(2, 4)
        -2.0

    Args:
        a (float): A number representing the number from which to subtract from.
        b (float): A number representing the number to subtract.

    Returns:
        float: A number representing the difference between `a` and `b`.
    """
    return float(a - b)


def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the difference of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0
        >>> multiply(2, 4)
        8.0

    Args:
        a (float): A number representing the first factor in the product.
        b (float): A number representing the second factor in the product.

    Returns:
        float: A number representing the product of `a` and `b`.
    """
    return float(a * b)


def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0
        >>> subtract(2, 4)
        -2.0

    Args:
        a (float): A number representing the number to divide.
        b (float): A number representing the divisor.

    Returns:
        float: A number representing the difference between `a` and `b`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
