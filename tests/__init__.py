"""Tests."""
# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'

import logging

import requests


def has_internet() -> bool:
    """Check if has internet."""
    try:
        if requests.get('https://google.com', timeout=1).ok:
            return True
    except requests.exceptions.ConnectionError:
        return False


if __name__ == '__main__':
    logging.debug(has_internet())
