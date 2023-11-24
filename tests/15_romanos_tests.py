#!/usr/bin/env python
"""# TODO: Atividade  15: Fatorar Romanos para que passe nos testes."""
__author__ = '@britodfbr'
import unittest
from types import FunctionType

import pytest
from incolume.py.tdd.romanos import Romanos


class TestRomanos(unittest.TestCase):
    def setUp(self):
        self.num = Romanos()

    def test_class_has_attr(self):
        assert 'romans' in Romanos.__dict__
        assert isinstance(Romanos.romans, dict)
        assert Romanos.romans.get('I') == 1
        assert isinstance(Romanos.arabics, dict)
        assert Romanos.arabics.get(1) == 'I'

    def test_class_has_func_0(self):
        assert 'calc_arabic' in Romanos.__dict__
        assert isinstance(Romanos.calc_arabic, FunctionType)
        assert hasattr(Romanos.calc_arabic, '__call__')

    def test_class_has_func_1(self):
        assert 'calc_arabic' in Romanos.__dict__
        assert isinstance(Romanos.calc_roman, FunctionType)
        assert hasattr(Romanos.calc_roman, '__call__')

    def test_arabic_single_number(self):
        assert self.num.calc_roman(1) == 'I'
        assert self.num.calc_roman(5) == 'V'
        assert self.num.calc_roman(10) == 'X'
        assert self.num.calc_roman(50) == 'L'
        assert self.num.calc_roman(100) == 'C'
        assert self.num.calc_roman(500) == 'D'
        assert self.num.calc_roman(1000) == 'M'

    def test_arabic_jugate_two_number_upper(self):
        assert self.num.calc_roman(11) == 'XI'
        assert self.num.calc_roman(1050) == 'ML'

    def test_arabic_jugate_more_number(self):
        assert self.num.calc_roman(3) == 'III'
        assert self.num.calc_roman(300) == 'CCC'
        assert self.num.calc_roman(440) == 'CDXL'
        assert self.num.calc_roman(1978) == 'MCMLXXVIII'

    def test_arabic_exceptions(self):
        with pytest.raises(
            ValueError, match='O argumento deve ser inteiro maior que zero.'
        ):
            self.num.calc_roman(0)

        with pytest.raises(TypeError, match='Esperado inteiro, obtido'):
            self.num.calc_roman('s')
            self.num.calc_roman(1.1)
            self.num.calc_roman(True)
            self.num.calc_roman('-1+0j')


if __name__ == '__main__':
    unittest.main()
