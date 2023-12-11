#!/usr/bin/python3
<<<<<<< HEAD
''' Integer addition in test driven development'''


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
=======
"""Adds two numbers"""


def add_integer(a, b=98):
    """
    Returns sum of a and b
    - Args :
        a: int or float
        b: int or float, default 98
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
>>>>>>> cbd273b01106d66c5827381bc1769c362ec7a85b
