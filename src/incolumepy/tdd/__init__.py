#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import toml
from pathlib import Path

__root__ = Path(__file__).parent.parent.parent.parent
__version__ = toml.load(__root__ / "pyproject.toml")['tool']['poetry']['version']
