import unittest
from incolumepy.veiculos.veiculos import Aeronave
from incolumepy.veiculos.veiculos import Veiculo

class Carro_test(unittest.TestCase):
    def setUp(self):
        self.veic = Aeronave()
        self.cls = Aeronave

    def tearDown(self):
        del self.veic

    def test_isInterface(self):
        self.assertTrue(isinstance(self.veic, Veiculo))
        self.assertTrue(issubclass(self.cls, Veiculo))

    def test_veiculo_interface_atributos(self):
        dir(self.veic)
        self.assertTrue(hasattr(self.veic, 'modelo'))
        self.assertTrue(hasattr(self.veic, 'fabricante'))
        self.assertTrue(hasattr(self.veic, 'velocidade'))
        self.assertFalse(hasattr(self.veic, 'cor'))
        
if __name__ == '__main__':
    unittest.main()
