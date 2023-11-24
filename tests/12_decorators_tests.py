#!/usr/bin/env python
"""# TODO: Atividade  12: implementar timeit para que passe nos testes."""
__author__ = '@britodfbr'
import unittest
from time import sleep

from incolume.py.tdd.utils.decorators import timeit


@timeit
def fake_method(value):
    sleep(1)
    return value


class TestDecorators(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_decorator(self):
        assert timeit.__qualname__ == 'timeit'
        assert timeit.__name__ == 'timeit'
        assert timeit.__annotations__ == {}
        assert timeit.__dict__ == {}

    def test_clousure_decorator_method(self):
        assert fake_method.__qualname__ == 'fake_method'
        assert fake_method.__name__ == 'fake_method'
        assert fake_method.__annotations__ == {}
        assert '__wrapped__' in fake_method.__dict__

    def test_timeit_0(self):
        """Aferir tipo retorno."""
        assert isinstance(fake_method(1), tuple)
        assert isinstance(fake_method(1)[0], int)
        assert isinstance(fake_method('1')[0], str)
        assert isinstance(fake_method(1)[1], float)

    def test_timeit_1(self):
        """Aferir retorno."""
        entradas = [(i, type(i)) for i in ['1', 1, 1.0]]

        for entrada, tipo in entradas:
            result = fake_method(entrada)[0]
            assert result == entrada
            assert isinstance(result, tipo)

    def test_timeit_2(self):
        """Aferir tempo."""
        assert fake_method('a')[1] >= 1
