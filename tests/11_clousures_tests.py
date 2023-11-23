#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  11: implementar multiple* para que passe nos testes

"""
__author__ = '@britodfbr'
import unittest
from incolume.py.tdd.utils.clousures import multiple, dobro


class TestClousure(unittest.TestCase):
    def setUp(self) -> None:
        self.triple = multiple(3)

    def test_clousure(self):
        self.assertEqual(multiple.__qualname__, 'multiple')
        self.assertEqual(multiple.__name__, 'multiple')
        self.assertEqual(multiple.__annotations__, {'mult': int})
        self.assertEqual(multiple.__dict__, {})

    def test_dobro(self):
        self.assertEqual(dobro.__qualname__, 'multiple.<locals>.x2')
        self.assertEqual(dobro.__name__, 'x2')
        self.assertEqual(dobro.__annotations__, {'value': int})
        self.assertEqual(dobro.__dict__, {})

    def test_result(self):
        self.assertEqual(dobro(3), 6)
        self.assertEqual(dobro(5), 10)
        self.assertEqual(dobro(7), 14)

    def test_triplo(self):
        self.assertEqual(self.triple.__qualname__, 'multiple.<locals>.x2')
        self.assertEqual(self.triple.__name__, 'x2')
        self.assertEqual(self.triple.__annotations__, {'value': int})
        self.assertEqual(self.triple(7), 21)
