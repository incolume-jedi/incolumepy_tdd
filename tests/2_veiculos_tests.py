import unittest
import abc
import datetime
from incolumepy.veiculos.veiculos import Veiculo


class Veiculo_tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.veic = Veiculo()

    def tearDown(self):
        del self.veic


    def test_veiculo_interface(self):
        self.assertTrue(Veiculo.__metaclass__ == abc.ABCMeta)
        with self.assertRaises(NotImplementedError):
            self.veic.acelerar(3)
            self.veic.frenar(3)

    def test_veiculo_interface_atributos(self):
        dir(self.veic)
        self.assertTrue(hasattr(self.veic, 'modelo'))
        self.assertTrue(hasattr(self.veic, 'fabricante'))
        self.assertTrue(hasattr(self.veic, 'velocidade'))
        self.assertFalse(hasattr(self.veic, 'cor'))

    def test_veiculo_interface_tipo(self):
        self.veic.tipo = 'Terrestre'
        self.veic.tipo = 'Aéreo'
        self.veic.tipo = 'AÉREO'
        self.veic.tipo = 'Aquático'
        self.veic.tipo = 'ESPACIAL'
        with self.assertRaises(AssertionError):
            self.veic.tipo = 'espaciale'
            self.veic.tipo = 'Aerio'

    def test_veiculo_interface_ano(self):

        self.veic.ano = 1976
        self.assertTrue(isinstance(self.veic.ano, datetime.datetime))
        self.assertEqual(self.veic.getAno(), '1976')

        self.veic.ano = '2018'
        self.assertTrue(isinstance(self.veic.ano, datetime.datetime))
        self.assertEqual(self.veic.getAno(), '2018')


if __name__ == '__main__':
    unittest.main()