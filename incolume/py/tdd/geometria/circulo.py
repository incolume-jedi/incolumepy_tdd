#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import pi


def circulo_area(raio: float) -> float:
    try:
        float(raio)
        if isinstance(raio, bool):
            raise AssertionError()
        if raio < 0 or isinstance(raio, bool):
            raise ValueError()
    except (AssertionError, TypeError, ValueError) as e:
        msg = 'raio deve ser numérico positivo maior que 0'
        if isinstance(e, ValueError):
            raise ValueError(msg)
        raise TypeError(msg)
    return pi * raio**2
