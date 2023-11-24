#!/usr/bin/env python
# -*- coding: utf-8 -*-


def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError('Somente operações com números naturais!')
    return a // b


def divisao(a, b):
    return a / b


def pot(a, b):
    return a**b
