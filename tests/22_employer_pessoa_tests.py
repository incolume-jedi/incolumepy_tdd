#!/usr/bin/env python
"""# TODO: Atividade  22: Proceder com as implementações necessárias para que passe nos testes.

Fatorar incolume.py.tdd.employers em 2 classes:
Pessoa(fullname, born, email, address, fone, cidade, estado)
Employer(Pessoa(), login, email, salario)
"""
__author__ = '@britodfbr'
import locale
import unittest
from datetime import datetime

import pytest
from faker import Faker
from incolume.py.tdd.employers import Employee, Pessoa


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fake = Faker('pt_BR')
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def setUp(self) -> None:
        pass

    def test_employer_is_pessoa(self):
        assert issubclass(Employee, Pessoa)

    def test_pessoa_nome(self):
        for i in range(1000):
            nome = f'{self.fake.first_name()} {self.fake.last_name()} {self.fake.last_name()}'
            pessoa = Pessoa(
                nome,
                self.fake.date(
                    pattern='%d/%m/%Y', end_datetime=datetime(2003, 1, 1),
                ),
            )
            assert nome == pessoa.fullname
            assert nome.split()[0] == pessoa.firstname
            assert nome.split()[-1] == pessoa.lastname
            assert ' '.join(nome.split()[1:-1]) == pessoa.middlename
            assert re.search('\\d{1,2} de \\w{3,} de \\d{4}', pessoa.born)
            dic = pessoa.to_dict()
            assert dic['firstname'] == nome.split()[0]
            assert dic['middlename'] == ' '.join(nome.split()[1:-1])

    def test_employer_nome(self):
        for i in range(1000):
            nome = f'{self.fake.first_name()} {self.fake.last_name()} {self.fake.last_name()}'
            pessoa = Employee(
                nome,
                self.fake.date(
                    pattern='%d/%m/%Y', end_datetime=datetime(2003, 1, 1),
                ),
                self.fake.random_int(min=900, max=9999, step=1),
            )
            pessoa.domain = 'test.incolume.com.br'
            assert nome == pessoa.fullname
            assert nome.split()[0] == pessoa.firstname
            assert nome.split()[-1] == pessoa.lastname
            assert ' '.join(nome.split()[1:-1]) == pessoa.middlename
            assert re.search('\\d{1,2} de \\w{3,} de \\d{4}', pessoa.born)

            dic = pessoa.to_dict()
            assert dic['firstname'] == nome.split()[0]
            assert dic['middlename'] == ' '.join(nome.split()[1:-1])

            assert pessoa.login.islower()
            assert re.search('[\\w.-]+@[a-z.]+', pessoa.email)

        with pytest.raises(Exception):
            dic = Employee(
                self.fake.name(), datetime.today().strftime('%d/%m/%Y'),
            ).to_dict()


if __name__ == '__main__':
    unittest.main()
