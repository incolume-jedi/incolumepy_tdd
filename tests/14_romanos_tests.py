#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from src.incolumepy.romanos import Romanos


class TestRomanos(unittest.TestCase):
    def setUp(self):
        self.num = Romanos()

    def test_romanos_single_number(self):
        self.assertEqual(self.num.i, 1)
        self.assertEqual(self.num.v, 5)
        self.assertEqual(self.num.x, 10)
        self.assertEqual(self.num.l, 50)
        self.assertEqual(self.num.c, 100)
        self.assertEqual(self.num.d, 500)
        self.assertEqual(self.num.m, 1000)

    def test_romanos_single_number_upper(self):
        self.assertEqual(self.num.I, 1)
        self.assertEqual(self.num.V, 5)
        self.assertEqual(self.num.X, 10)
        self.assertEqual(self.num.L, 50)
        self.assertEqual(self.num.C, 100)
        self.assertEqual(self.num.D, 500)
        self.assertEqual(self.num.M, 1000)

    def test_romanos_jugate_two_number(self):
        self.assertEqual(self.num.ii, 2)
        self.assertEqual(self.num.iv, 4)
        self.assertEqual(self.num.vi, 6)
        self.assertEqual(self.num.ix, 9)
        self.assertEqual(self.num.xi, 11)
        self.assertEqual(self.num.il, 49)
        self.assertEqual(self.num.li, 51)
        self.assertEqual(self.num.ic, 99)
        self.assertEqual(self.num.ci, 101)
        self.assertEqual(self.num.id, 499)
        self.assertEqual(self.num.di, 501)
        self.assertEqual(self.num.im, 999)
        self.assertEqual(self.num.mi, 1001)

    def test_romanos_jugate_two_number_upper(self):
        self.assertEqual(self.num.II, 2)
        self.assertEqual(self.num.IV, 4)
        self.assertEqual(self.num.VI, 6)
        self.assertEqual(self.num.IX, 9)
        self.assertEqual(self.num.XI, 11)
        self.assertEqual(self.num.IL, 49)
        self.assertEqual(self.num.LI, 51)
        self.assertEqual(self.num.IC, 99)
        self.assertEqual(self.num.CI, 101)
        self.assertEqual(self.num.ID, 499)
        self.assertEqual(self.num.DI, 501)
        self.assertEqual(self.num.IM, 999)
        self.assertEqual(self.num.MI, 1001)

    def test_romanos_jugate_more_number(self):
        self.assertEqual(self.num.III, 3)
        self.assertEqual(self.num.XLviii, 48)
        self.assertEqual(self.num.MCCCLXXXVIII, 1388)
        self.assertEqual(self.num.MCDXLIX, 1449)
        self.assertEqual(self.num.MDCCCLXXVIII, 1878)
        self.assertEqual(self.num.MDCDLXXVIII, 1978)

    def test_romanos_exceptions(self):
        with self.assertRaisesRegex(ValueError, "Não pertencem aos numerais romanos"):
            self.num.s
            self.num.G
            self.num.yH
            self.num.JJK
            self.num.ij
            self.num.Kx


if __name__ == '__main__':
    unittest.main()
