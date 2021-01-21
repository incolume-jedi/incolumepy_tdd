import unittest
from src.incolumepy.tdd.utils.decode.morse import decodeMorse

# TODO: Atividade  26: Proceder com as implementações necessárias para que passe nos testes


class MyTestCase(unittest.TestCase):
    def test_something(self):
        """Example from description"""
        self.assertEqual(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')


if __name__ == '__main__':
    unittest.main()
