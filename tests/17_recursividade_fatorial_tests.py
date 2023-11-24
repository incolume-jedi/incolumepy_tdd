#!/usr/bin/env python
"""# TODO: Atividade  17: implementar fatorial para que passe nos testes."""
__author__ = '@britodfbr'
import unittest
from types import FunctionType
from unittest import mock

from incolume.py.tdd.sequences.fatorial import fatorial


class RecursividadeTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_function(self):
        assert isinstance(fatorial, FunctionType)
        assert hasattr(fatorial, '__call__')
        assert fatorial.__qualname__ == 'fatorial'
        assert fatorial.__name__ == 'fatorial'
        assert fatorial.__annotations__ == {'pos': int, 'return': int}

    def test_values(self):
        assert fatorial(1) == 1
        assert fatorial(2) == 2
        assert fatorial(3) == 6
        assert fatorial(6) == 720
        assert fatorial(10) == 3628800

    def test_values_1(self):
        assert [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800] == [fatorial(x) for x in range(11)]

    def test_fuction_called(self):
        with mock.patch(
            'incolume.py.tdd.sequences.fatorial.fatorial', autospec=True,
        ) as mock_fact:
            # mock_fact.__rmul__ = lambda x: fatorial(x)
            entrada = 99
            result = fatorial(entrada)
            assert mock_fact.called
            # print(result)
            assert re.search('__rmul__', str(result))

    def test_recursividade_1(self):
        with mock.patch(
            'incolume.py.tdd.sequences.fatorial.fatorial',
        ) as mock_fact:
            entrada = 99
            fatorial(entrada)
            # print(mock_fact.call_args)
            assert mock_fact.call_args == mock.call(entrada - 1)
            # print(mock_fact.call_args_list)
            assert mock.call(entrada - 1) in mock_fact.call_args_list

    def test_recursividade_2(self):
        with mock.patch(
            'incolume.py.tdd.sequences.fatorial.fatorial',
        ) as mock_fact:
            for i in range(1, 99, -2):
                expected = i - 1
                fatorial(i)
                assert mock_fact.called
                assert mock_fact.call_count == expected
                assert mock_fact.call_args == mock.call(expected)


if __name__ == '__main__':
    unittest.main()
