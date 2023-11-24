# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import hashlib
from pathlib import Path


def hash_md5_0(file):
    result = hashlib.md5(Path(file).read_bytes())
    return result.hexdigest()


def hash_sha1_0(file):
    result = hashlib.sha1(Path(file).read_bytes())
    return result.hexdigest()
