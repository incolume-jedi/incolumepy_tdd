#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  15: Fatorar Romanos para que passe nos testes

"""
__author__ = '@britodfbr'
import unittest
from incolume.py.tdd.romanos import Romanos
from types import FunctionType


class TestRomanos(unittest.TestCase):
    def setUp(self):
        self.num = Romanos()

    def test_class_has_attr(self):
        self.assertIn('romans', Romanos.__dict__)
        self.assertIsInstance(Romanos.romans, dict)
        self.assertEqual(Romanos.romans.get('I'), 1)
        self.assertIsInstance(Romanos.arabics, dict)
        self.assertEqual(Romanos.arabics.get(1), 'I')

    def test_class_has_func_0(self):
        self.assertIn('calc_arabic', Romanos.__dict__)
        self.assertIsInstance(Romanos.calc_arabic, FunctionType)
        self.assertTrue(hasattr(Romanos.calc_arabic, '__call__'))

    def test_class_has_func_1(self):
        self.assertIn('calc_arabic', Romanos.__dict__)
        self.assertIsInstance(Romanos.calc_roman, FunctionType)
        self.assertTrue(hasattr(Romanos.calc_roman, '__call__'))

    def test_arabic_single_number(self):
        self.assertEqual(self.num.calc_roman(1), 'I')
        self.assertEqual(self.num.calc_roman(5), 'V')
        self.assertEqual(self.num.calc_roman(10), 'X')
        self.assertEqual(self.num.calc_roman(50), 'L')
        self.assertEqual(self.num.calc_roman(100), 'C')
        self.assertEqual(self.num.calc_roman(500), 'D')
        self.assertEqual(self.num.calc_roman(1000), 'M')

    def test_arabic_jugate_two_number_upper(self):
        self.assertEqual(self.num.calc_roman(11), 'XI')
        self.assertEqual(self.num.calc_roman(1050), 'ML')

    def test_arabic_jugate_more_number(self):
        self.assertEqual(self.num.calc_roman(3), 'III')
        self.assertEqual(self.num.calc_roman(300), 'CCC')
        self.assertEqual(self.num.calc_roman(440), 'CDXL')
        self.assertEqual(self.num.calc_roman(1978), 'MCMLXXVIII')

    def test_arabic_exceptions(self):
        with self.assertRaisesRegex(ValueError, "O argumento deve ser inteiro maior que zero."):
            self.num.calc_roman(0)

        with self.assertRaisesRegex(TypeError, "Esperado inteiro, obtido"):
            self.num.calc_roman("s")
            self.num.calc_roman(1.1)
            self.num.calc_roman(True)
            self.num.calc_roman("-1+0j")


if __name__ == '__main__':
    unittest.main()
