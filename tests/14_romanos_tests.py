"""# TODO: Atividade  14: Fatorar Romanos para que passe nos testes."""
__author__ = '@britodfbr'
import unittest

import pytest
from incolume.py.tdd.romanos import Romanos


class TestRomanos(unittest.TestCase):
    def setUp(self):
        self.num = Romanos()

    def test_romanos_single_number(self):
        assert self.num.i == 1
        assert self.num.v == 5
        assert self.num.x == 10
        assert self.num.l == 50
        assert self.num.c == 100
        assert self.num.d == 500
        assert self.num.m == 1000

    def test_romanos_single_number_upper(self):
        assert self.num.I == 1
        assert self.num.V == 5
        assert self.num.X == 10
        assert self.num.L == 50
        assert self.num.C == 100
        assert self.num.D == 500
        assert self.num.M == 1000

    def test_romanos_jugate_two_number(self):
        assert self.num.ii == 2
        assert self.num.iv == 4
        assert self.num.vi == 6
        assert self.num.ix == 9
        assert self.num.xi == 11
        assert self.num.il == 49
        assert self.num.li == 51
        assert self.num.ic == 99
        assert self.num.ci == 101
        assert self.num.id == 499
        assert self.num.di == 501
        assert self.num.im == 999
        assert self.num.mi == 1001

    def test_romanos_jugate_two_number_upper(self):
        assert self.num.II == 2
        assert self.num.IV == 4
        assert self.num.VI == 6
        assert self.num.IX == 9
        assert self.num.XI == 11
        assert self.num.IL == 49
        assert self.num.LI == 51
        assert self.num.IC == 99
        assert self.num.CI == 101
        assert self.num.ID == 499
        assert self.num.DI == 501
        assert self.num.IM == 999
        assert self.num.MI == 1001

    def test_romanos_jugate_more_number(self):
        assert self.num.III == 3
        assert self.num.XLviii == 48
        assert self.num.MCCCLXXXVIII == 1388
        assert self.num.MCDXLIX == 1449
        assert self.num.MDCCCLXXVIII == 1878
        assert self.num.MDCDLXXVIII == 1978

    def test_romanos_exceptions(self):
        with pytest.raises(
            ValueError, match='Não pertencem aos numerais romanos'
        ):
            self.num.s
            self.num.G
            self.num.yH
            self.num.JJK
            self.num.ij
            self.num.Kx


if __name__ == '__main__':
    unittest.main()
