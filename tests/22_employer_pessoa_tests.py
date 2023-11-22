#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  22: Proceder com as implementações necessárias para que passe nos testes

Fatorar incolumepy.tdd.employers em 2 classes:
Pessoa(fullname, born, email, address, fone, cidade, estado)
Employer(Pessoa(), login, email, salario)
"""
__author__ = '@britodfbr'
import unittest
import locale
from faker import Faker
from incolumepy.tdd.employers import Employee, Pessoa
from datetime import datetime


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fake = Faker("pt_BR")
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    def setUp(self) -> None:
        pass

    def test_employer_is_pessoa(self):
        self.assertTrue(issubclass(Employee, Pessoa))

    def test_pessoa_nome(self):
        for i in range(1000):
            nome = F"{self.fake.first_name()} {self.fake.last_name()} {self.fake.last_name()}"
            pessoa = Pessoa(nome, self.fake.date(pattern="%d/%m/%Y", end_datetime=datetime(2003, 1, 1)))
            self.assertEqual(nome, pessoa.fullname)
            self.assertEqual(nome.split()[0], pessoa.firstname)
            self.assertEqual(nome.split()[-1], pessoa.lastname)
            self.assertEqual(' '.join(nome.split()[1:-1]), pessoa.middlename)
            self.assertRegex(pessoa.born, r'\d{1,2} de \w{3,} de \d{4}')
            dic = pessoa.to_dict()
            self.assertEqual(dic['firstname'], nome.split()[0])
            self.assertEqual(dic['middlename'], ' '.join(nome.split()[1:-1]))

    def test_employer_nome(self):
        for i in range(1000):
            nome = F"{self.fake.first_name()} {self.fake.last_name()} {self.fake.last_name()}"
            pessoa = Employee(
                nome,
                self.fake.date(pattern="%d/%m/%Y", end_datetime=datetime(2003, 1, 1)),
                self.fake.random_int(min=900, max=9999, step=1)
            )
            pessoa.domain = 'test.incolume.com.br'
            self.assertEqual(nome, pessoa.fullname)
            self.assertEqual(nome.split()[0], pessoa.firstname)
            self.assertEqual(nome.split()[-1], pessoa.lastname)
            self.assertEqual(' '.join(nome.split()[1:-1]), pessoa.middlename)
            self.assertRegex(pessoa.born, r'\d{1,2} de \w{3,} de \d{4}')

            dic = pessoa.to_dict()
            self.assertEqual(dic['firstname'], nome.split()[0])
            self.assertEqual(dic['middlename'], ' '.join(nome.split()[1:-1]))

            self.assertTrue(pessoa.login.islower())
            self.assertRegex(pessoa.email, r'[\w.-]+@[a-z.]+')

        with self.assertRaises(Exception):
            dic = Employee(self.fake.name(), datetime.today().strftime("%d/%m/%Y")).to_dict()


if __name__ == '__main__':
    unittest.main()
