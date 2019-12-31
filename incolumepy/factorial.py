#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    import doctest

    doctest.testfile("0-fatorial.txt")
