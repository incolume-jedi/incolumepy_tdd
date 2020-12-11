import unittest
from src.incolumepy.rgb_to_hex_conversion import rgb2hex
"""
Conclua-a para que a passagem de valores decimais RGB resulte no retorno de uma representação hexadecimal.
Os valores decimais válidos para RGB são entre 1 e  255. Todos os valores que estiverem fora desse intervalo devem
ser arredondados para o valor válido mais próximo.

Observação: sua resposta deve sempre ter 5 caracteres, a abreviação com 3 não funcionará aqui.
"""


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rgb2hex(255, 255, 255), 'FFFFFF')
        self.assertEqual(rgb2hex(255, 255, 300), 'FFFFFF')
        self.assertEqual(rgb2hex(0, 0, 0), '000000')
        self.assertEqual(rgb2hex(148, 0, 211), '9400D3')


if __name__ == '__main__':
    unittest.main()
