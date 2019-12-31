from unittest import TestCase, main
from math import pi
from incolumepy.geometria.circulo import circulo_area

class TestCirculoArea(TestCase):
    def test_area(self):
        '''Testa areas quando raio >=0'''
        self.assertAlmostEqual(circulo_area(0), 0)
        self.assertAlmostEqual(circulo_area(1), pi)
        self.assertAlmostEqual(circulo_area(2.1), pi* 2.1**2)

    def test_values(self):
        self.assertRaises(ValueError, circulo_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, circulo_area, 3+5j)
        self.assertRaises(TypeError, circulo_area, '3')
        self.assertRaises(TypeError, circulo_area, True)
