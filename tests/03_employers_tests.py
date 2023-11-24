#!/usr/bin/env python
"""# TODO: Atividade  3: implementar Employee para que passe nos testes."""
__author__ = '@britodfbr'
import datetime as dt
from datetime import datetime
from unittest import TestCase, main

import pytest
from incolume.py.tdd.employers import Employee


class EmployersTests(TestCase):
    @classmethod
    def setUpClass(cls):
        ...

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
        assert self.emp1.domain == 'incolume.com.br'
        assert self.emp2.domain == 'incolume.com.br'
        assert self.emp3.domain == 'incolume.com.br'

    def test_fristname(self):
        self.emp1.firstname = 'francisco'
        self.emp2.firstname = 'joana'
        assert self.emp1.firstname == 'Francisco'
        assert self.emp2.firstname == 'Joana'
        assert self.emp3.firstname == 'Marcos'

    def test_email(self):
        self.assertRaises(TypeError, self.emp1.domain)
        self.assertRaises(TypeError, self.emp2.domain)
        self.assertRaises(TypeError, self.emp3.domain)

        self.emp1.domain = 'incolume.com.br'
        assert self.emp1.email == 'jose.silva@incolume.com.br'
        assert self.emp2.email == 'maria.souza@incolume.com.br'
        assert self.emp3.email == 'marcos.santos@incolume.com.br'

        self.emp3.domain = 'exemplo.com.br'
        assert self.emp1.email == 'jose.silva@exemplo.com.br'
        assert self.emp2.email == 'maria.souza@exemplo.com.br'

    def test_lastname(self):
        assert self.emp1.lastname == 'Silva'
        assert self.emp2.lastname == 'Souza'
        assert self.emp3.lastname == 'Santos'

        self.emp3.lastname = 'nascimento'
        assert self.emp3.lastname == 'Nascimento'

    def test_fullname(self):
        self.emp1 = Employee('josé ferreira da silva', '10/10/2004', 960)
        assert self.emp1.fullname == 'José Ferreira da Silva'
        assert self.emp2.fullname == 'Maria Francisca de Souza'
        assert self.emp3.fullname == 'Marcos Oliveira Santos'

        self.emp1.firstname = 'francisco'
        self.emp2.firstname = 'joana'
        assert self.emp1.fullname == 'Francisco Ferreira da Silva'
        assert self.emp2.fullname == 'Joana Francisca de Souza'

        self.emp3.lastname = 'nascimento'
        assert self.emp3.fullname == 'Marcos Oliveira Nascimento'

    def test_middlename(self):
        assert self.emp1.middlename == 'Ferreira da'
        assert self.emp2.middlename == 'Francisca de'
        assert self.emp3.middlename == 'Oliveira'

        self.emp1.middlename = 'nascimento'
        self.emp2.middlename = 'nascimento'
        self.emp3.middlename = 'nascimento'

        assert self.emp1.middlename == 'Nascimento'
        assert self.emp2.middlename == 'Nascimento'
        assert self.emp3.middlename == 'Nascimento'

        assert self.emp1.fullname == 'José Nascimento Silva'
        assert self.emp2.fullname == 'Maria Nascimento Souza'
        assert self.emp3.fullname == 'Marcos Nascimento Santos'

        self.emp3.middlename = 'nascimento dos'
        assert self.emp3.middlename == 'Nascimento dos'
        assert self.emp3.fullname == 'Marcos Nascimento dos Santos'

    def test_salario(self):
        assert self.emp1.salario == 960
        assert self.emp2.salario == 1000
        assert self.emp3.salario == 1000

    def test_aumento_salario_int(self):
        """Aumento percentual de salário."""
        self.emp1.aumento_salario(5)
        self.emp2.aumento_salario(8)
        self.emp3.aumento_salario(10)

        assert 960 * 1.05 == self.emp1.salario
        assert 1000 * 1.08 == self.emp2.salario
        assert 1000 * 1.1 == self.emp3.salario

    def test_aumento_salario_float(self):
        self.emp3.aumento_salario(0.1)
        assert 1000 * 1.1 == self.emp3.salario

    def test_date_born(self):
        # assert isinstance(self.emp1.born, datetime), "Objeto não é instancia de datetime.datetime"
        assert datetime, type(self.emp1.born)
        assert self.emp1.born == '06 de setembro de 2000'
        assert self.emp2.born == '06 de setembro de 1978'
        assert self.emp3.born == '01 de janeiro de 1985'

        self.emp2.born = '5/5/2004'
        assert self.emp2.born == '05 de maio de 2004'

    def test_date_born_Raiser(self):
        with pytest.raises(ValueError):
            self.emp3.born = datetime.today().strftime('%d/%m/%Y')
            self.emp3.born = (
                datetime.today() + dt.timedelta(days=1)
            ).strftime('%d/%m/%Y')
            self.emp3.born = (
                datetime.today() + dt.timedelta(weeks=1)
            ).strftime('%d/%m/%Y')
            self.emp3.born = (
                datetime.today() + dt.timedelta(weeks=5)
            ).strftime('%d/%m/%Y')
            self.emp3.born = (
                datetime.today() + dt.timedelta(weeks=15)
            ).strftime('%d/%m/%Y')
            self.emp3.born = (
                datetime.today() + dt.timedelta(weeks=53)
            ).strftime('%d/%m/%Y')

        with pytest.raises(ValueError, match='Data de Nascimento inferior a permitida'):
            self.emp3.born = (
                datetime.today() + dt.timedelta(days=352)
            ).strftime('%d/%m/%Y')
            self.emp3.born = (
                datetime.today() + dt.timedelta(days=5475)
            ).strftime('%d/%m/%Y')


if __name__ == '__main__':
    main()
