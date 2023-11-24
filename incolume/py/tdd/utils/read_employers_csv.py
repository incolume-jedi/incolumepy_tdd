# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import csv
import pandas as pd
from pathlib import Path
from incolume.py.tdd.employers import Employee


class EmployeerCorp(Employee):
    def __init__(
        self,
        fullname,
        born,
        salario,
        domain,
        fone,
        cep,
        address,
        bairro,
        cidade,
        estado,
    ):
        super().__init__(fullname, born, salario)
        self.__domain = domain
        self.fone = fone
        self.cep = cep
        self.address = address
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def to_dict(self):
        dic = super().to_dict()
        # print(dic)
        dic['fone'] = self.fone
        dic['cep'] = self.cep
        dic['address'] = self.address
        dic['bairro'] = self.bairro
        dic['cidade'] = self.cidade
        dic['estado'] = self.estado
        return dic


def load_employers(csvfile: (str, Path)):
    df = pd.read_csv(csvfile)
    d = {}
    for i, employer in df.iterrows():
        # print(i, employer.nome, employer.born, employer.telefone)
        d[i] = EmployeerCorp(
            fullname=employer.nome,
            born=employer.born,
            domain='tabajara.com.br',
            salario=employer.salario,
            address=employer.address,
            fone=employer.telefone,
            cep=employer.cep,
            bairro=employer.bairro,
            cidade=employer.cidade,
            estado=employer.estado,
        )
    return d


def dump_employers_xlsx(emps: list, xlsxfile: (str, Path)):
    xlsxfile = Path(xlsxfile).with_suffix('.xlsx')
    df = pd.DataFrame(emp.to_dict() for emp in emps)
    df.to_excel(xlsxfile)


def run():   # pragma: no cover
    dic = load_employers('/tmp/tmpxmyrhiwt.csv')
    print(len(dic))
    print(dic)
    print(dic[0].fullname, dic[0].login, dic[0].email)
    print(dic[0].to_dict())
    dump_employers_xlsx(dic.values(), '/tmp/test.xlsx')


if __name__ == '__main__':
    run()
