"""# TODO: Atividade  26: Morse
Proceder com as implementações necessárias para que passe nos testes.

Decodificar Código Morse
"""
__author__ = '@britodfbr'
import unittest

from incolume.py.tdd.utils.decode.morse import decodeMorse


class MyTestCase(unittest.TestCase):
    def test_decode0(self):
        assert decodeMorse('.... . -.--   .--- ..- -.. .') == 'HEY JUDE'

    def test_decode1(self):
        assert decodeMorse('.. -. -.-. --- .-.. ..- -- .') == 'INCOLUME'

    def test_decode2(self):
        assert decodeMorse('- .-. . .. -. .- -- . -. - ---') == 'TREINAMENTO'

    def test_decode3(self):
        assert decodeMorse('   .--. -.-- - .... --- -.') == 'PYTHON'


if __name__ == '__main__':
    unittest.main()
