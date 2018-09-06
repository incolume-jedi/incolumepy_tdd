import unittest
import calc

class Calc_test(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calc.soma(2, 2), 4)
        self.assertEqual(calc.soma(2, -2), 0)

    def test_sub(self):
        self.assertEqual(calc.sub(2, 2), 0)
        self.assertEqual(calc.sub(2, -2), 4)

    def test_mult(self):
        self.assertEqual(calc.mult(2, 2), 4)
        self.assertEqual(calc.mult(2, -2), -4)

    def test_divisao(self):
        self.assertEqual(calc.divisao(2, 2), 1)
        self.assertEqual(calc.divisao(2, -2), -1)
        self.assertEqual(calc.divisao(1, 2), 0.5)
        self.assertEqual(calc.divisao(-1, 2), -0.5)
        self.assertRaises(calc.divisao(1, 0), ZeroDivisionError)

    def test_div(self):
        self.assertEqual(calc.div(3, 2), 1)
        self.assertEqual(calc.div(1, 2), 0)
        self.assertRaises(calc.div(1, 0), ValueError)
        self.assertRaises(calc.div(1, -1), ValueError)
        self.assertRaises(calc.div(-1, 1), ValueError)

    def test_pot(self):
        self.assertEqual(calc.pot(2, 2), 4)
        self.assertEqual(calc.pot(10, 2), 100)
        self.assertEqual(calc.pot(10, -2), 0.01)

if __name__ == '__main__':
    unittest.main()