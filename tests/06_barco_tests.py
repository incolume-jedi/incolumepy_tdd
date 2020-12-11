import unittest
from src.incolumepy.veiculos.barco import Barco


class TestBarco(unittest.TestCase):
    def setUp(self):
        self.veic = Barco()
        self.cls = Barco

    def tearDown(self):
        del self.veic

    def test_isInterface(self):
        self.assertTrue(isinstance(self.veic, Barco))
        self.assertTrue(issubclass(self.cls, Barco))

    def test_veiculo_interface_atributos(self):
        dir(self.veic)
        self.assertTrue(hasattr(self.veic, 'modelo'))
        self.assertTrue(hasattr(self.veic, 'fabricante'))
        self.assertTrue(hasattr(self.veic, 'velocidade'))
        self.assertFalse(hasattr(self.veic, 'cor'))


if __name__ == '__main__':
    unittest.main()
