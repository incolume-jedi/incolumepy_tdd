#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import doctest

# TODO: Atividade  1: implementar fatorial para que passe nos testes


def fatorial(pos: int) -> int:
    if (pos + 1) == pos:
        raise OverflowError("n too large")
    if pos < 0:
        raise ValueError("n must be >= 0")
    if not (int(pos) or math.floor(pos)) == pos:
        raise ValueError("n must be exact integer")
    if pos <= 1:
        return 1
    else:
        return pos * fatorial(pos - 1)


if __name__ == "__main__":
    doctest.testfile("01-fatorial.txt")
