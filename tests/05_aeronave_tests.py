"""# TODO: Atividade  5: implementar Aeronave para que passe nos testes."""
__author__ = '@britodfbr'
import unittest

from incolume.py.tdd.veiculos.aeronaves import Aeronave


class TestAeronave(unittest.TestCase):
    def setUp(self):
        self.veic = Aeronave()
        self.cls = Aeronave

    def tearDown(self):
        del self.veic

    def test_isInterface(self):
        assert isinstance(self.veic, Aeronave)
        assert issubclass(self.cls, Aeronave)

    def test_veiculo_interface_atributos(self):
        dir(self.veic)
        assert hasattr(self.veic, 'modelo')
        assert hasattr(self.veic, 'fabricante')
        assert hasattr(self.veic, 'velocidade')
        assert not hasattr(self.veic, 'cor')


if __name__ == '__main__':
    unittest.main()
