"""# TODO: Atividade  4: implementar Veiculo para que passe nos testes."""
__author__ = '@britodfbr'
import unittest

import pytest
from incolume.py.tdd.veiculos.veiculos import Veiculo, abc, datetime


class VeiculoTests(unittest.TestCase):
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
        assert Veiculo.__metaclass__ == abc.ABCMeta
        with pytest.raises(NotImplementedError):
            self.veic.acelerar(3)
            self.veic.frenar(3)

    def test_veiculo_interface_atributos(self):
        dir(self.veic)
        assert hasattr(self.veic, 'modelo')
        assert hasattr(self.veic, 'fabricante')
        assert hasattr(self.veic, 'velocidade')
        assert not hasattr(self.veic, 'cor')

    def test_veiculo_interface_tipo(self):
        assert 'terrestre'.upper() in Veiculo.categoria
        assert 'aéreo'.upper() in Veiculo.categoria
        assert 'aquático'.upper() in Veiculo.categoria
        assert 'espacial'.upper() in Veiculo.categoria
        self.veic.tipo = 'Terrestre'
        self.veic.tipo = 'Aéreo'
        self.veic.tipo = 'AÉREO'
        self.veic.tipo = 'Aquático'
        self.veic.tipo = 'ESPACIAL'

        with pytest.raises(AssertionError):
            self.veic.tipo = 'espaciale'
            self.veic.tipo = 'Aerio'

        with pytest.raises(AssertionError, match='Categoria não disponível'):
            self.veic.tipo = 'espaciale'
            self.veic.tipo = 'Aerio'

    def test_veiculo_interface_ano(self):

        self.veic.ano = 1976
        assert isinstance(self.veic.ano, datetime)
        assert self.veic.getAno() == '1976'

        self.veic.ano = '2018'
        assert isinstance(self.veic.ano, datetime)
        assert self.veic.getAno() == '2018'

        with pytest.raises(ValueError, match='Informe o Ano com 4 algarismos'):
            self.veic.ano = 'aaaa'


if __name__ == '__main__':
    unittest.main()
