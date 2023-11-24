#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  16: implementar fibonacci para que passe nos testes
"""
__author__ = '@britodfbr'
import unittest
import mock
from types import FunctionType
from incolume.py.tdd.sequences.fibonacci import fibonacci


class RecursividadeTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_package(self):
        self.assertIsNotNone(__package__)

    def test_function(self):
        self.assertIsInstance(fibonacci, FunctionType)
        self.assertTrue(hasattr(fibonacci, '__call__'))
        self.assertEqual(fibonacci.__qualname__, 'fibonacci')
        self.assertEqual(fibonacci.__name__, 'fibonacci')
        self.assertEqual(
            fibonacci.__annotations__, {'pos': int, 'return': int}
        )

    def test_recursividade(self):
        with mock.patch(
            'incolume.py.tdd.sequences.fibonacci.fibonacci'
        ) as mock_fib:
            fibonacci(3)
            self.assertTrue(mock_fib.called)
            self.assertGreaterEqual(mock_fib.call_count, 2)

    def test_recursividade_1(self):
        with mock.patch(
            'incolume.py.tdd.sequences.fibonacci.fibonacci'
        ) as mock_fib:
            fibonacci(3)
            self.assertTrue(mock_fib.called)
            self.assertGreaterEqual(mock_fib.call_count, 2)

    def test_recursividade_2(self):
        with mock.patch(
            'incolume.py.tdd.sequences.fibonacci.fibonacci'
        ) as mock_fib:
            for i in range(1, 5, -1):
                expected = i - 1
                fibonacci(i)
                self.assertTrue(mock_fib.called)
                self.assertEqual(mock_fib.call_count, expected)

    def test_values(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(10), 55)

    def test_values_1(self):
        self.assertEqual(
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
            [fibonacci(x) for x in range(11)],
        )


if __name__ == '__main__':
    unittest.main()
