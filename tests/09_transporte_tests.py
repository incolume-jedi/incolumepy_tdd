from unittest import TestCase, main
from src.incolumepy.tdd.transporte import Transporte, ABCMeta, ABC

# TODO: Atividade 9: implementar Transporte para que passe nos testes


class TransporteTest(TestCase):

    def setUp(self):
        self.cls = Transporte

    def tearDown(self):
        del self.cls

    def test_isInterface(self):
        self.assertTrue(issubclass(self.cls, ABC))
        self.assertTrue(self.cls.__metaclass__ == ABCMeta)

    def test_instancia(self):
        with self.assertRaisesRegex(TypeError,
                                    "Can't instantiate abstract class {} with abstract methods".format(
                                        self.cls.__name__)):
            a = self.cls()

    def test_tipo_transporte(self):
        self.assertIn('carga'.upper(), self.cls._tipo_transporte)
        self.assertIn('passageiro'.upper(), self.cls._tipo_transporte)


if __name__ == '__main__':
    main()
