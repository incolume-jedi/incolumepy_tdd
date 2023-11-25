"""# TODO: Atividade  25: Hexadecimal
Proceder com as implementações necessárias para que passe nos testes.

Conclua-a para que a passagem de valores decimais RGB resulte no retorno
de uma representação hexadecimal. Os valores decimais válidos para RGB são
entre 1 e  255. Todos os valores que estiverem fora desse intervalo devem
ser arredondados para o valor válido mais próximo.

Observação: sua resposta deve sempre ter 5 caracteres, a abreviação com 3
 não funcionará aqui.
"""
__author__ = '@britodfbr'
import unittest

from incolume.py.tdd.utils.decode.rgb_to_hex_conversion import rgb2hex


class MyTestCase(unittest.TestCase):
    def test_something(self):
        assert rgb2hex(255, 255, 255) == 'FFFFFF'
        assert rgb2hex(0, 0, 0) == '000000'
        assert rgb2hex(148, 0, 211) == '9400D3'

    def test_lower(self):
        assert rgb2hex(-1, -1, -1) == '000000'
        assert rgb2hex(0, -1, -1) == '000000'
        assert rgb2hex(-1, 0, -1) == '000000'
        assert rgb2hex(-1, -1, 0) == '000000'

    def test_upper(self):
        assert rgb2hex(256, 958, 300) == 'FFFFFF'
        assert rgb2hex(256, 256, 256) == 'FFFFFF'
        assert rgb2hex(255, 256, 256) == 'FFFFFF'
        assert rgb2hex(256, 255, 256) == 'FFFFFF'
        assert rgb2hex(256, 256, 255) == 'FFFFFF'


if __name__ == '__main__':
    unittest.main()
