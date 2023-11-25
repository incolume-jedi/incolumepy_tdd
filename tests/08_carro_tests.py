"""# TODO: Atividade  8: implementar Carro para que passe nos testes."""
__author__ = '@britodfbr'
import unittest

from incolume.py.tdd.veiculos.carro import Carro


class TestCarro(unittest.TestCase):
    def setUp(self):
        self.veic = Carro()

    def tearDown(self):
        del self.veic

    def test_isInterface(self):
        assert isinstance(self.veic, Carro)
        assert issubclass(Carro, Carro)

    def test_veiculo_interface_atributos(self):
        dir(self.veic)
        assert hasattr(self.veic, 'modelo')
        assert hasattr(self.veic, 'fabricante')
        assert hasattr(self.veic, 'velocidade')
        assert not hasattr(self.veic, 'cor')


if __name__ == '__main__':
    unittest.main()
