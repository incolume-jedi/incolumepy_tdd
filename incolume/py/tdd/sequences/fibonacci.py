#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path

__package__ = '.'.join(Path(__file__).parts[-4:]).strip('.py')


def fibonacci(pos: int) -> int:
    if pos <= 1:
        return pos
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)


if __name__ == '__main__':
    print(__package__)
