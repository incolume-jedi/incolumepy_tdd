#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from incolumepy.tdd import __version__

setup(name='incolumepy_tdd',
      version=__version__,
      description='Python Utilities for trainning',
      author='Ricardo *Brito* do Nascimento',
      author_email='contato@incolume.com.br',
      url='https://gitlab.com/development-incolume/treinamentos/incolumepy_tdd',
      test_suite='nose.collector',
      tests_require='nose',
      )
