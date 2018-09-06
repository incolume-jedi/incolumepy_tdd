import unittest
import datetime as dt
from datetime import datetime
from employers import Employee


class Employers_tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.emp1 = Employee('José Ferreira da Silva', '6/9/2000', 960)
        self.emp2 = Employee('Maria Francisca de Souza', '6/9/1978', 1000)
        self.emp3 = Employee('Marcos Oliveira  Santos', '1/1/1985', 1000)

    def tearDown(self):
        pass


    def test_domain(self):
        self.emp1.domain = 'incolume.com.br'
        self.assertEqual(self.emp1.domain, 'incolume.com.br')
        self.assertEqual(self.emp2.domain, 'incolume.com.br')
        self.assertEqual(self.emp3.domain, 'incolume.com.br')

    def test_fristname(self):
        self.emp1.firstname = 'francisco'
        self.emp2.firstname = 'joana'
        self.assertEqual(self.emp1.firstname, 'Francisco')
        self.assertEqual(self.emp2.firstname, 'Joana')
        self.assertEqual(self.emp3.firstname, 'Marcos')

    def test_email(self):
        self.assertRaises(ValueError, self.emp1.domain)
        self.assertRaises(ValueError, self.emp2.domain)
        self.assertRaises(ValueError, self.emp3.domain)

        self.emp1.domain = 'incolume.com.br'
        self.assertEqual(self.emp1.email, 'jose.silva@incolume.com.br')
        self.assertEqual(self.emp2.email, 'maria.souza@incolume.com.br')
        self.assertEqual(self.emp3.email, 'marcos.santos@incolume.com.br')

    def test_lastname(self):
        self.assertEqual(self.emp1.lastname, 'Silva')
        self.assertEqual(self.emp2.lastname, 'Souza')
        self.assertEqual(self.emp3.lastname, 'Santos')

        self.emp3.lastname = 'nascimento'
        self.assertEqual(self.emp3.lastname, 'Nascimento')

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'José Ferreira da Silva')
        self.assertEqual(self.emp2.fullname, 'Maria Francisca de Souza')
        self.assertEqual(self.emp3.fullname, 'Marcos Oliveira Santos')

        self.emp1.firstname = 'francisco'
        self.emp2.firstname = 'joana'
        self.assertEqual(self.emp1.fullname, 'Francisco Ferreira da Silva')
        self.assertEqual(self.emp2.fullname, 'Joana Francisca de Souza')

        self.emp3.lastname = 'nascimento'
        self.assertEqual(self.emp2.fullname, 'Marco Oliveira Nascimento')


    def test_middlename(self):
        self.assertEqual(self.emp1.middlename, 'Ferreira da')
        self.assertEqual(self.emp2.middlename, 'Francisca de')
        self.assertEqual(self.emp3.middlename, 'Oliveira')

        self.emp1.middlename = 'nascimento'
        self.emp2.middlename = 'nascimento'
        self.emp3.middlename = 'nascimento'

        self.assertEqual(self.emp1.middlename, 'Nascimento')
        self.assertEqual(self.emp2.middlename, 'Nascimento')
        self.assertEqual(self.emp3.middlename, 'Nascimento')

        self.assertEqual(self.emp1.fullname, 'José Nascimento Silva')
        self.assertEqual(self.emp2.fullname, 'Maria Nascimento Souza')
        self.assertEqual(self.emp3.fullname, 'Marcos Nascimento Santos')

        self.emp3.middlename = 'nascimento dos'
        self.assertEqual(self.emp3.middlename, 'Nascimento dos')
        self.assertEqual(self.emp3.fullname, 'Marcos Nascimento dos Santos')

    def test_salario(self):
        self.assertEqual(self.emp1.salario, 960)
        self.assertEqual(self.emp2.salario, 1000)
        self.assertEqual(self.emp3.salario, 1000)

    def test_aumento_salario(self):
        self.emp1.aumento_salario(5)
        self.emp1.aumento_salario(8)
        self.emp1.aumento_salario(10)

        self.assertEqual(self.emp1.salario, 960*1.05)
        self.assertEqual(self.emp2.salario, 960*1.08)
        self.assertEqual(self.emp3.salario, 960*1.10)


    def test_date_born(self):
        assert isinstance(self.emp1.born, datetime), "Objeto não é o instancia de datetime.datetime"
        self.assertEqual(self.emp1.born, '06 de setembro de 2000')
        self.assertEqual(self.emp2.born, '06 de setembro de 1978')
        self.assertEqual(self.emp3.born, '01 de janeiro de 1985')

        with self.assertRaises(ValueError):
            self.emp3.born = datetime.today()
            self.emp3.born = datetime.today() + dt.timedelta(days=1)
            self.emp3.born = datetime.today() + dt.timedelta(weeks=1)
            self.emp3.born = datetime.today() + dt.timedelta(weeks=5)
            self.emp3.born = datetime.today() + dt.timedelta(weeks=15)
            self.emp3.born = datetime.today() + dt.timedelta(weeks=53)


        self.emp2.born = '5/5/2005'
        self.assertEqual(self.emp2.born, '05 de maio de 2005')


if __name__ == '__main__':
    unittest.main()