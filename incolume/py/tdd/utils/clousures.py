#!/usr/bin/env python
# -*- coding: utf-8 -*-


def multiple(mult: int):
    def x2(value: int, *args, **kwargs):
        return mult * value

    return x2


dobro = multiple(2)
