#!/usr/bin/env python
"""# TODO: Atividade  16: implementar fibonacci para que passe nos testes."""
__author__ = '@britodfbr'
import unittest
from types import FunctionType
from unittest import mock

from incolume.py.tdd.sequences.fibonacci import fibonacci


class RecursividadeTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_package(self):
        assert __package__ is not None

    def test_function(self):
        assert isinstance(fibonacci, FunctionType)
        assert hasattr(fibonacci, '__call__')
        assert fibonacci.__qualname__ == 'fibonacci'
        assert fibonacci.__name__ == 'fibonacci'
        assert fibonacci.__annotations__ == {'pos': int, 'return': int}

    def test_recursividade(self):
        with mock.patch(
            'incolume.py.tdd.sequences.fibonacci.fibonacci',
        ) as mock_fib:
            fibonacci(3)
            assert mock_fib.called
            assert mock_fib.call_count >= 2

    def test_recursividade_1(self):
        with mock.patch(
            'incolume.py.tdd.sequences.fibonacci.fibonacci',
        ) as mock_fib:
            fibonacci(3)
            assert mock_fib.called
            assert mock_fib.call_count >= 2

    def test_recursividade_2(self):
        with mock.patch(
            'incolume.py.tdd.sequences.fibonacci.fibonacci',
        ) as mock_fib:
            for i in range(1, 5, -1):
                expected = i - 1
                fibonacci(i)
                assert mock_fib.called
                assert mock_fib.call_count == expected

    def test_values(self):
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(10) == 55

    def test_values_1(self):
        assert [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55] == [
            fibonacci(x) for x in range(11)
        ]


if __name__ == '__main__':
    unittest.main()
