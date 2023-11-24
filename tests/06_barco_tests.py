#!/usr/bin/env python
"""# TODO: Atividade  6: implementar Barco para que passe nos testes."""
__author__ = '@britodfbr'
import unittest

from incolume.py.tdd.veiculos.barco import Barco


class TestBarco(unittest.TestCase):
    def setUp(self):
        self.veic = Barco()
        self.cls = Barco

    def tearDown(self):
        del self.veic

    def test_isInterface(self):
        assert isinstance(self.veic, Barco)
        assert issubclass(self.cls, Barco)

    def test_veiculo_interface_atributos(self):
        dir(self.veic)
        assert hasattr(self.veic, 'modelo')
        assert hasattr(self.veic, 'fabricante')
        assert hasattr(self.veic, 'velocidade')
        assert not hasattr(self.veic, 'cor')


if __name__ == '__main__':
    unittest.main()
