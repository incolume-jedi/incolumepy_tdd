#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
from time import time


def timeit(func):
    time0 = time()

    @wraps(func)
    def counttime(*args, **kwargs):
        result = func(*args, **kwargs)
        return result, time() - time0

    return counttime
