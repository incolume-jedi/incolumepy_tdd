#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  5: implementar Aeronave para que passe nos testes

"""
__author__ = '@britodfbr'
import unittest
from incolume.py.tdd.veiculos.aeronaves import Aeronave


class TestAeronave(unittest.TestCase):
    def setUp(self):
        self.veic = Aeronave()
        self.cls = Aeronave

    def tearDown(self):
        del self.veic

    def test_isInterface(self):
        self.assertTrue(isinstance(self.veic, Aeronave))
        self.assertTrue(issubclass(self.cls, Aeronave))

    def test_veiculo_interface_atributos(self):
        dir(self.veic)
        self.assertTrue(hasattr(self.veic, 'modelo'))
        self.assertTrue(hasattr(self.veic, 'fabricante'))
        self.assertTrue(hasattr(self.veic, 'velocidade'))
        self.assertFalse(hasattr(self.veic, 'cor'))


if __name__ == '__main__':
    unittest.main()
