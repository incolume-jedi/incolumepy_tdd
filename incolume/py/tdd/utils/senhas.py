# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import string
from random import sample, shuffle


def senhas(length: int = 6) -> str:
    """ """
    if length < 6:
        raise ValueError('Tamanho mínimo aceito: 6 caracteres')

    pw = []
    pw += sample(string.ascii_lowercase, 1)
    pw += sample(string.ascii_uppercase, 1)
    pw += sample(string.digits, 1)
    pw += sample(string.ascii_letters, length - 3)
    shuffle(pw)
    return ''.join(pw)
