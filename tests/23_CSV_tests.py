#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  23: Proceder com as implementações necessárias para que passe nos testes

1 - Criar uma nova classe que herda de incolumepy.tdd.employers.Employee:
EmployeeCorp[Employee](fullname, born, address, fone, estado, cidade, login, email, login)

2 - Construir um programa que carregue instancias de EmployeeCorp contendo, todas as informações de todos
 os funcionários a partir de um arquivo CSV, Defina o domínio como "tabajara.com.br" e
  grave as informações produzidas em um arquivo XLSX.
"""
__author__ = '@britodfbr'
import unittest
import re
import csv
import pandas as pd
from collections import namedtuple
from random import randint
from pathlib import Path
from faker import Faker
from tempfile import NamedTemporaryFile
from datetime import datetime
from src.incolumepy.tdd import employers
from src.incolumepy.tdd.utils.read_employers_csv import EmployeerCorp, load_employers, dump_employers_xlsx


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fake = Faker("pt_BR")
        cls.fout = NamedTemporaryFile(delete=False, suffix='.csv', mode='wt')
        cls.csvfile = cls.fout.name
        cls.xlsxfile = Path(cls.csvfile).with_suffix('.xlsx')
        headers = ["nome", "born", "salario", "telefone", "cep", "address", "bairro", "cidade", "estado"]
        writer = csv.DictWriter(cls.fout, fieldnames=headers)
        writer.writeheader()
        user = namedtuple('funcionario', '')
        for e in range(1000):
            user.fullname = f"{cls.fake.first_name()} {cls.fake.last_name()} {cls.fake.last_name()}"
            user.born = cls.fake.date(pattern="%d/%m/%Y", end_datetime=datetime(2003, 1, 1))
            user.salario = cls.fake.random_int(min=900, max=9999, step=1)
            user.domain = "exemplo.incolume.com.br"
            # user.fone = cls.fake.phone_number()
            user.fone = "+55 61 9{}{}-{}{}".format(randint(70, 99), randint(70, 99), randint(70, 99), randint(11, 99))
            user.address, user.bairro, value = re.split(r'\n', cls.fake.address())
            # user.estado = re.split(r' |/', value)[-1]
            user.estado = 'Distrito Federal'
            # user.cep = re.split(r' |/', value)[0]
            user.cep = "72.{}-{}".format(randint(100, 999), randint(100, 999))
            # user.cidade = ''.join(re.split(r' |/', value)[1:-1])
            user.cidade = 'Brasília'
            d = {
                k: v
                for k, v
                in zip(
                    headers,
                    [
                        user.fullname, user.born,
                        user.salario, user.fone, user.cep, user.bairro, user.address,
                        user.cidade, user.estado
                    ]
                )
            }
            print(d)
            writer.writerow(d)
        print(cls.fout.name)
        cls.fout.close()

    def test_issubclass(self):
        self.assertTrue(issubclass(employers.Employee, employers.Pessoa))
        self.assertTrue(issubclass(EmployeerCorp, employers.Employee))
        self.assertTrue(issubclass(EmployeerCorp, employers.Pessoa))

    def test_load_employers_assign(self):
        self.assertEqual(load_employers.__annotations__, {'csvfile': (str, Path)})

    def test_load_employers_on_dict(self):
        loadeds = load_employers(self.csvfile)
        self.assertIsInstance(loadeds, dict)
        self.assertEqual(len(loadeds), 1000)

    def test_load_employers_dict_content(self):
        with open(self.csvfile) as csvfile:
            # print(csvfile.name)
            loadeds = load_employers(self.csvfile)
            next(csvfile)
            record = next(csvfile)
            # print(record)
            # print(loadeds.get(0).fullname)
            self.assertIsInstance(loadeds[0], EmployeerCorp)
            self.assertIn(loadeds[0].fullname.lower(), record.lower())

    def test_dump_employers_xlsx_assing(self):
        self.assertEqual(dump_employers_xlsx.__annotations__, {'emps': list, 'xlsxfile': (str, Path)})

    def test_dump_employers_xlsx_created(self):
        dump_employers_xlsx(load_employers(self.csvfile).values(), self.xlsxfile)
        self.assertTrue(Path(self.xlsxfile).is_file())

    def test_dump_employers_xlsx_fields(self):
        dump_employers_xlsx(load_employers(self.csvfile).values(), self.xlsxfile)
        df0 = pd.read_csv(self.csvfile)
        df1 = pd.read_excel(self.xlsxfile, engine='openpyxl')
        self.assertEqual(df0.shape[0], df1.shape[0])
        self.assertIn('firstname', list(df1.columns))
        self.assertIn('middlename', list(df1.columns))
        self.assertIn('lastname', list(df1.columns))
        self.assertIn('born', list(df1.columns))
        self.assertIn('email', list(df1.columns))
        self.assertIn('login', list(df1.columns))
        self.assertIn('fone', list(df1.columns))
        self.assertIn('cep', list(df1.columns))
        self.assertIn('bairro', list(df1.columns))
        self.assertIn('cidade', list(df1.columns))
        self.assertIn('estado', list(df1.columns))

    def test_dump_employers_xlsx_content(self):
        dump_employers_xlsx(load_employers(self.csvfile).values(), self.xlsxfile)
        df0 = pd.read_csv(self.csvfile)
        df1 = pd.read_excel(self.xlsxfile, engine='openpyxl')
        # print(df0.born, df1.born)
        df0.born = pd.to_datetime(df0.born, format='%d/%m/%Y')
        df1.born = pd.to_datetime(df1.born, format='%d de %B de %Y')
        self.assertEqual(df0.iloc[100].born, df1.iloc[100].born)
        # print(df0.iloc[3].nome)
        id = randint(1, 1000)
        self.assertIn(df1.iloc[id].firstname, df0.iloc[id].nome)
        self.assertIn(df1.iloc[id].middlename, df0.iloc[id].nome)
        self.assertIn(df1.iloc[id].lastname, df0.iloc[id].nome)


if __name__ == '__main__':
    unittest.main()
