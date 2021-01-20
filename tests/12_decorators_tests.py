#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from time import sleep
from src.incolumepy.utils.decorators import timeit

# TODO: Atividade  12: implementar timeit para que passe nos testes


@timeit
def fake_method(value):
    sleep(1)
    return value


class TestDecorators(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_decorator(self):
        self.assertEqual(timeit.__qualname__, 'timeit')
        self.assertEqual(timeit.__name__, 'timeit')
        self.assertEqual(timeit.__annotations__, {})
        self.assertEqual(timeit.__dict__, {})

    def test_clousure_decorator_method(self):
        self.assertEqual(fake_method.__qualname__, 'fake_method')
        self.assertEqual(fake_method.__name__, 'fake_method')
        self.assertEqual(fake_method.__annotations__, {})
        self.assertIn('__wrapped__', fake_method.__dict__)

    def test_timeit_0(self):
        """Aferir tipo retorno"""
        self.assertIsInstance(fake_method(1), tuple)
        self.assertIsInstance(fake_method(1)[0], int)
        self.assertIsInstance(fake_method('1')[0], str)
        self.assertIsInstance(fake_method(1)[1], float)

    def test_timeit_1(self):
        """Aferir retorno"""
        entradas = [(i, type(i)) for i in ['1', 1, 1.0]]

        for entrada, tipo in entradas:
            result = fake_method(entrada)[0]
            self.assertEqual(result, entrada)
            self.assertIsInstance(result, tipo)

    def test_timeit_2(self):
        """Aferir tempo"""
        self.assertGreaterEqual(fake_method('a')[1], 1)
