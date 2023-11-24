#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  2: implementar calculadora (calc) para que passe nos testes
"""
__author__ = '@britodfbr'
import unittest
from incolume.py.tdd import calc


class CalcTest(unittest.TestCase):
    """verifica os valores de resultado"""

    def test_soma(self):
        self.assertEqual(calc.soma(2, 2), 4)
        self.assertEqual(calc.soma(2, -2), 0)

    def test_sub(self):
        """verifica os valores de resultado"""
        self.assertEqual(calc.sub(2, 2), 0)
        self.assertEqual(calc.sub(2, -2), 4)

    def test_mult(self):
        """verifica os valores de resultado"""
        self.assertEqual(calc.mult(2, 2), 4)
        self.assertEqual(calc.mult(2, -2), -4)

    def test_divisao(self):
        """verifica os valores de resultado e possíveis exceções"""
        self.assertEqual(calc.divisao(2, 2), 1)
        self.assertEqual(calc.divisao(2, -2), -1)
        self.assertEqual(calc.divisao(1, 2), 0.5)
        self.assertEqual(calc.divisao(-1, 2), -0.5)
        self.assertRaises(ZeroDivisionError, calc.divisao, 1, 0)

    def test_div(self):
        """verifica os valores de resultado"""
        self.assertEqual(calc.div(3, 2), 1)
        self.assertEqual(calc.div(1, 2), 0)

    # @unittest.skip("Erro de analise")
    def test_div_raises(self):
        """Checa a mensagem da exceção"""
        self.assertRaises(ValueError, calc.div, 1, 0)
        with self.assertRaises(ValueError):
            calc.div(1, 0)
            calc.div(1, -1)
            calc.div(-1, 1)

    def test_div_raises_msg(self):
        with self.assertRaisesRegex(
            ValueError, r'Somente operações com números naturais!'
        ):
            calc.div(1, 0)
            calc.div(1, -1)
            calc.div(-1, 1)

    def test_pot(self):
        """verifica os valores de resultado"""
        self.assertEqual(calc.pot(2, 2), 4)
        self.assertEqual(calc.pot(10, 2), 100)
        self.assertEqual(calc.pot(10, -2), 0.01)


if __name__ == '__main__':
    unittest.main()
