# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'

import requests


def has_internet():
    try:
        if requests.get('https://google.com').ok:
            return True
    except requests.exceptions.ConnectionError:
        return False


if __name__ == '__main__':
    print(has_internet())
