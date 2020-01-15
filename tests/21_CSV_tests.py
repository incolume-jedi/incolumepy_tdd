"""
Fatorar incolumepy.employers em 2 classes:
Pessoa(fullname, born, email, address, fone, cidade, estado)
Employer(Pessoa(), login, email, salario)
"""
import unittest
from faker import Faker
from tempfile import NamedTemporaryFile
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
            user.login = normalize(
                'NFKD',
                f"{user.firstname}{''.join([i[0] for i in user.middlename.split()])}{user.lastname[0]}"
            ).encode('ASCII', 'ignore').decode('ASCII').lower()
            user.domain = "exemplo.incolume.com.br"
            user.fone = cls.fake.phone_number()
            user.address = cls.fake.address()
            user.cidade = cls.fake.city()
            user.estado = cls.fake.state()
            # print(user.__dict__)
            # print(f"{user.fullname}, {user.firstname}, {user.lastname}, "
            #       f"{user.email}, {user.born}, {user.salario:.2f}, {user.address}, {user.cidade}, {user.estado}")
            headers = ["nome", "login", "email", "born", "salario", "telefone", "address", "cidade", "estado"]
            writer = csv.DictWriter(cls.fout, fieldnames=headers)
            d = {
                k: v
                for k, v
                in zip(
                    headers,
                    [
                        user.fullname, user.login, user.email, user.born,
                        user.salario, user.fone, user.address, user.cidade, user.estado
                    ]
                )
            }
            print(d)
            writer.writerow(d)
        print(cls.fout.name)
        cls.fout.close()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
