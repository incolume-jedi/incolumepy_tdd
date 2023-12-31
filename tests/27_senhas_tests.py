"""# TODO: Atividade  27: Senhas.
Proceder com as implementações necessárias para que passe nos testes."""
__author__ = '@britodfbr'
import re
import unittest

import pytest
from incolume.py.tdd.utils.senhas import senhas


class MyTestCase(unittest.TestCase):
    """As senhas geradas possuem o seguinte critério:
    - 6 ou + caracteres;
    - conter pelo menos 1 letras minusculas;
    - conter pelo menos 1 letras maiusculas;
    - conter pelo menos 1 numeros;
    - ser formada por caracteres alphanumericos;

    """

    def setUp(self) -> None:
        self.regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$'

    def test_senha_validation(self):
        assert re.match(self.regex, senhas())

    def test_length_min(self):
        for i in range(100):
            assert len(senhas()) == 6
        with pytest.raises(
            ValueError, match='Tamanho mínimo aceito: 6 caracteres'
        ):
            senhas(4)

    def test_alphanumeric(self):
        assert isinstance(senhas(), str)


if __name__ == '__main__':
    unittest.main()
