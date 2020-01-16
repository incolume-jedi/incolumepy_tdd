"""
Fatorar incolumepy.employers em 2 classes:
Pessoa(fullname, born, email, address, fone, cidade, address)
Employer(Pessoa(), login, email, salario)
"""
import unittest
import re
from faker import Faker
from tempfile import NamedTemporaryFile
from incolumepy.pessoa import Pessoa
from incolumepy.employers import Employee, normalize
from datetime import datetime
from incolumepy.utils.read_employers_csv import csv


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fake = Faker("pt_BR")
        cls.fout = NamedTemporaryFile(delete=False, mode='wt')
        for e in range(1000):
            user = Employee(
                f"{cls.fake.first_name()} {cls.fake.last_name()} {cls.fake.last_name()}",
                cls.fake.date(pattern="%d/%m/%Y", end_datetime=datetime(2003, 1, 1)),
                cls.fake.random_int(min=900, max=9999, step=1)
            )
            user.domain = "exemplo.incolume.com.br"
            user.fone = cls.fake.phone_number()
            values = [
                bairro, address, cep, cidade, estado \
                for bairro, address, x in cls.fake.address().split('\n') for cep, cidade, estado in re.split(' |/', x)]
            user.bairro, user.address, user.cep, user.cidade, user.estado = values
            headers = ["nome", "login", "email", "born", "salario", "telefone", "cep", "address", "bairro"]
            writer = csv.DictWriter(cls.fout, fieldnames=headers)
            d = {
                k: v
                for k, v
                in zip(
                    headers,
                    [
                        user.fullname, user.login, user.email, user.born,
                        user.salario, user.fone, user.cep, user.bairro, user.address
                    ]
                )
            }
            print(d)
            writer.writerow(d)
        print(cls.fout.name)
        cls.fout.close()

    def test_something(self):
        self.assertIsInstance(Employee, Pessoa)


if __name__ == '__main__':
    unittest.main()
