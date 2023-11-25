"""# TODO: Atividade  7: implementar Bicicleta para que passe nos testes."""
__author__ = '@britodfbr'
import unittest

from incolume.py.tdd.veiculos.bicicleta import Bicicleta


class TestBicicleta(unittest.TestCase):
    def setUp(self):
        self.veic = Bicicleta()

    def tearDown(self):
        del self.veic

    def test_isInterface(self):
        assert isinstance(self.veic, Bicicleta)
        assert issubclass(Bicicleta, Bicicleta)

    def test_veiculo_interface_atributos(self):
        dir(self.veic)
        assert hasattr(self.veic, 'modelo')
        assert hasattr(self.veic, 'fabricante')
        assert hasattr(self.veic, 'velocidade')
        assert not hasattr(self.veic, 'cor')


if __name__ == '__main__':
    unittest.main()
