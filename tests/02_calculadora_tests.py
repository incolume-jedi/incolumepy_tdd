"""# TODO: Atividade  2: Calculadora.
implementar calculadora (calc) para que passe nos testes."""
__author__ = '@britodfbr'
import unittest

import pytest
from incolume.py.tdd import calc


class CalcTest(unittest.TestCase):
    """verifica os valores de resultado."""

    def test_soma(self):
        assert calc.soma(2, 2) == 4
        assert calc.soma(2, -2) == 0

    def test_sub(self):
        """Verifica os valores de resultado."""
        assert calc.sub(2, 2) == 0
        assert calc.sub(2, -2) == 4

    def test_mult(self):
        """Verifica os valores de resultado."""
        assert calc.mult(2, 2) == 4
        assert calc.mult(2, -2) == -4

    def test_divisao(self):
        """Verifica os valores de resultado e possíveis exceções."""
        assert calc.divisao(2, 2) == 1
        assert calc.divisao(2, -2) == -1
        assert calc.divisao(1, 2) == 0.5
        assert calc.divisao(-1, 2) == -0.5
        self.assertRaises(ZeroDivisionError, calc.divisao, 1, 0)

    def test_div(self):
        """Verifica os valores de resultado."""
        assert calc.div(3, 2) == 1
        assert calc.div(1, 2) == 0

    # @unittest.skip("Erro de analise")
    def test_div_raises(self):
        """Checa a mensagem da exceção."""
        self.assertRaises(ValueError, calc.div, 1, 0)
        with pytest.raises(ValueError):
            calc.div(1, 0)
            calc.div(1, -1)
            calc.div(-1, 1)

    def test_div_raises_msg(self):
        with pytest.raises(
            ValueError, match=r'Somente operações com números naturais!'
        ):
            calc.div(1, 0)
            calc.div(1, -1)
            calc.div(-1, 1)

    def test_pot(self):
        """Verifica os valores de resultado."""
        assert calc.pot(2, 2) == 4
        assert calc.pot(10, 2) == 100
        assert calc.pot(10, -2) == 0.01


if __name__ == '__main__':
    unittest.main()
