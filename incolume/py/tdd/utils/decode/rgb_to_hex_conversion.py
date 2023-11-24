# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'


def rgb2hex(r: int, g: int, b: int) -> str:
    r = 0 if r < 0 else r
    r = 255 if r > 255 else r
    g = 0 if g < 0 else g
    g = 255 if g > 255 else g
    b = 0 if b < 0 else b
    b = 255 if b > 255 else b

    return f'{r:02x}{g:02x}{b:02x}'.upper()
