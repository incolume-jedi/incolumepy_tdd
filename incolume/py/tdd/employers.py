#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from unicodedata import normalize
from incolume.py.tdd.pessoa import Pessoa
import locale


class Employee(Pessoa):
    __domain = ''

    def __init__(self, fullname, born, salario):
        super().__init__(fullname, born)
        self.salario = salario
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def aumento_salario(self, percent: (int, float)):
        if isinstance(percent, float):
            self.salario *= 1 + percent
        else:
            self.salario *= 1 + percent / 100

    @property
    def login(self):
        return (
            normalize(
                'NFKD',
                f"{self.firstname}{''.join([i[0] for i in self.middlename.split()])}{self.lastname[0]}",
            )
            .encode('ASCII', 'ignore')
            .decode('ASCII')
            .lower()
        )

    @property
    def email(self):
        return (
            normalize(
                'NFKD',
                '{}.{}@{}'.format(
                    self.firstname, self.lastname, self.domain
                ).lower(),
            )
            .encode('ASCII', 'ignore')
            .decode('ASCII')
        )

    @property
    def domain(self) -> str:
        return Employee.__domain

    @domain.setter
    def domain(self, value: str) -> None:
        Employee.__domain = value

    @property
    def born(self):
        return self.__born.strftime('%d de %B de %Y')

    @born.setter
    def born(self, value):
        born = datetime.strptime(value, '%d/%m/%Y')
        idade = abs(born - datetime.today())
        if idade.days < 5475:
            raise ValueError('Data de Nascimento inferior a permitida')
        self.__born = born

    def to_dict(self):
        dic = super().to_dict()
        dic['email'] = self.email
        dic['login'] = self.login
        return dic
