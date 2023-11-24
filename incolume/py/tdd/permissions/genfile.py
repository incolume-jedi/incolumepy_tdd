#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Permission:
    u: int = 0
    g: int = 0
    o: int = 0


def create(
    content: (str, bytes), filename: (str, Path), permissions: str
) -> bool:
    filename = Path(filename)
    if isinstance(content, bytes):
        filename.write_bytes(content)
    else:
        filename.write_text(content)

    # p = namedtuple('permissions', 'u g o')
    # perms = p(0, 0, 0)
    perms = Permission(0, 0, 0)
    if not len(permissions) == 9:
        raise AttributeError('Bad permission length')

    if 'r' in permissions[:3]:
        perms.u += 4

    if 'w' in permissions[:3]:
        perms.u += 2

    if 'x' in permissions[:3]:
        perms.u += 1

    if 'r' in permissions[3:6]:
        perms.g += 4

    if 'w' in permissions[3:6]:
        perms.g += 2

    if 'x' in permissions[3:6]:
        perms.g += 1

    if 'r' in permissions[-3:]:
        perms.o += 4

    if 'w' in permissions[-3:]:
        perms.o += 2

    if 'x' in permissions[-3:]:
        perms.o += 1

    # print(perms.__dict__)
    filename.chmod(int('{u}{g}{o}'.format(**perms.__dict__), 8))
    # print(filename.name)
    return filename.is_file()
