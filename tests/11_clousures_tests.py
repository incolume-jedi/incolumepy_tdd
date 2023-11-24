"""# TODO: Atividade  11: implementar multiple* para que passe nos testes."""
__author__ = '@britodfbr'
import unittest

from incolume.py.tdd.utils.clousures import dobro, multiple


class TestClousure(unittest.TestCase):
    def setUp(self) -> None:
        self.triple = multiple(3)

    def test_clousure(self):
        assert multiple.__qualname__ == 'multiple'
        assert multiple.__name__ == 'multiple'
        assert multiple.__annotations__ == {'mult': int}
        assert multiple.__dict__ == {}

    def test_dobro(self):
        assert dobro.__qualname__ == 'multiple.<locals>.x2'
        assert dobro.__name__ == 'x2'
        assert dobro.__annotations__ == {'value': int}
        assert dobro.__dict__ == {}

    def test_result(self):
        assert dobro(3) == 6
        assert dobro(5) == 10
        assert dobro(7) == 14

    def test_triplo(self):
        assert self.triple.__qualname__ == 'multiple.<locals>.x2'
        assert self.triple.__name__ == 'x2'
        assert self.triple.__annotations__ == {'value': int}
        assert self.triple(7) == 21
