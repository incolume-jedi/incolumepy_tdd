#!/usr/bin/env python
"""# TODO: Atividade 9: implementar Transporte para que passe nos testes."""
__author__ = '@britodfbr'
from unittest import TestCase, main

import pytest
from incolume.py.tdd.transporte import ABC, ABCMeta, Transporte


class TransporteTest(TestCase):
    def setUp(self):
        self.cls = Transporte

    def tearDown(self):
        del self.cls

    def test_isInterface(self):
        assert issubclass(self.cls, ABC)
        assert self.cls.__metaclass__ == ABCMeta

    def test_instancia(self):
        with pytest.raises(TypeError, match=rf".*Can't instantiate abstract class {self.cls.__name__} with abstract method.*"):
            self.cls()

    def test_tipo_transporte(self):
        assert 'carga'.upper() in self.cls._tipo_transporte
        assert 'passageiro'.upper() in self.cls._tipo_transporte


if __name__ == '__main__':
    main()
