#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import mock
from types import FunctionType
from src.incolumepy.sequences.fatorial import fatorial

# TODO: Atividade  17: implementar fatorial para que passe nos testes


class RecursividadeTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_function(self):
        self.assertIsInstance(fatorial, FunctionType)
        self.assertTrue(hasattr(fatorial, '__call__'))
        self.assertEqual(fatorial.__qualname__, 'fatorial')
        self.assertEqual(fatorial.__name__, 'fatorial')
        self.assertEqual(fatorial.__annotations__, {'pos': int, 'return': int})

    def test_values(self):
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(3), 6)
        self.assertEqual(fatorial(6), 720)
        self.assertEqual(fatorial(10), 3628800)

    def test_values_1(self):
        self.assertEqual([1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800], [fatorial(x) for x in range(11)])

    def test_fuction_called(self):
        with mock.patch('incolumepy.sequences.fatorial.fatorial', autospec=True) as mock_fact:
            # mock_fact.__rmul__ = lambda x: fatorial(x)
            entrada = 99
            result = fatorial(entrada)
            self.assertTrue(mock_fact.called)
            # print(result)
            self.assertRegex(str(result), r'__rmul__')

    def test_recursividade_1(self):
        with mock.patch('incolumepy.sequences.fatorial.fatorial') as mock_fact:
            entrada = 99
            fatorial(entrada)
            # print(mock_fact.call_args)
            self.assertEqual(mock_fact.call_args, mock.call(entrada - 1))
            # print(mock_fact.call_args_list)
            self.assertIn(mock.call(entrada - 1), mock_fact.call_args_list)

    def test_recursividade_2(self):
        with mock.patch('incolumepy.sequences.fatorial.fatorial') as mock_fact:
            for i in range(1, 99, -2):
                expected = i - 1
                fatorial(i)
                self.assertTrue(mock_fact.called)
                self.assertEqual(mock_fact.call_count, expected)
                self.assertEqual(mock_fact.call_args, mock.call(expected))


if __name__ == '__main__':
    unittest.main()
