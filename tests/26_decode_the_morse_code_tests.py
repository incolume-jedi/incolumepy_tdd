#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  26: Proceder com as implementações necessárias para que passe nos testes

Decodificar Código Morse
"""
__author__ = '@britodfbr'
import unittest
from incolume.py.tdd.utils.decode.morse import decodeMorse


class MyTestCase(unittest.TestCase):
    def test_decode0(self):
        self.assertEqual(
            decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE'
        )

    def test_decode1(self):
        self.assertEqual(
            decodeMorse('.. -. -.-. --- .-.. ..- -- .'), 'INCOLUME'
        )

    def test_decode2(self):
        self.assertEqual(
            decodeMorse('- .-. . .. -. .- -- . -. - ---'), 'TREINAMENTO'
        )

    def test_decode3(self):
        self.assertEqual(decodeMorse('   .--. -.-- - .... --- -.'), 'PYTHON')


if __name__ == '__main__':
    unittest.main()
