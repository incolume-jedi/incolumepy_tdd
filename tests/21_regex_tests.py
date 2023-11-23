#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  21: Proceder com as implementações necessárias para que passe nos testes

Regras para identificar bandeira do cartão de crédito: https://pastebin.com/CiKUtZRU
"""
__author__ = '@britodfbr'
import unittest
import locale
import rstr
import pytest
from faker import Factory
from faker.providers import internet
from faker.providers import date_time
from incolume.py.tdd.utils.regex import re
from incolume.py.tdd.utils.regex import is_ccredito_amex
from incolume.py.tdd.utils.regex import is_ccredito_diners
from incolume.py.tdd.utils.regex import is_ccredito_master
from incolume.py.tdd.utils.regex import is_ccredito_visa
from incolume.py.tdd.utils.regex import is_date
from incolume.py.tdd.utils.regex import isemail
from incolume.py.tdd.utils.regex import isfone
from incolume.py.tdd.utils.regex import is_ipv4
from incolume.py.tdd.utils.regex import is_ipv6
from incolume.py.tdd.utils.regex import is_url
from itertools import chain


def fake_factory():
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    FakeFactory = Factory.create('pt_BR')
    FakeFactory.add_provider(date_time)
    FakeFactory.add_provider(internet)
    return FakeFactory


class TestRegex:
    """Class TestRegex for 21_regex."""

    @pytest.mark.parametrize(
        'entrance',
        chain(
            [
                rstr.xeger(
                    r'(?:\+5{2} )?\(?([14689][1-9]|2[12478]|'
                    r'3[1234578]|5[1345]|7[134579])\)? \d?\d{4}[ -]?\d{4}'
                )
                for _ in range(100)
            ],
            [
                '+55 21 5555-5555',
                '+55 22 5555 5555',
                '+55 24 95555 5555',
                '+55 75 5555 5555',
                '+55 27 5555 5555',
                '+55 28 5555 5555',
                '+55 51 1693-9021',
                '+55 53 16939021',
                '+55 54 1693-9021',
                '+55 55 1693-9021',
                '+55 (11) 99999 9999',
                '+55 61 99999-9999',
                '+55 62 99999-9999',
            ],
        ),
    )
    def test_fone(self, entrance):
        assert isfone(entrance)


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        cls.FakeFactory = Factory.create('pt_BR')
        cls.FakeFactory.add_provider(date_time)
        cls.FakeFactory.add_provider(internet)

    def setUp(self) -> None:
        self.FakeFactory.credit_card_expire(start="now", end="+10y", date_format="%m/%y")

    def re_validate(self):
        self.assertEqual(__file__, re.match(r'tests'))

    def test_is_ccredito_amex(self):
        self.assertEqual(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='amex')), True)
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='diners')))
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='mastercard')))
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='visa')))
        self.assertFalse(is_ccredito_amex("VISA 16 digit \nVinicius Novaes \n4210582570068192 07/28 \nCVC: 846"))
        with self.assertRaisesRegex(TypeError, "required string"):
            is_ccredito_amex(4210582570068192)

    def test_is_ccredito_diners(self):
        self.assertEqual(is_ccredito_diners(self.FakeFactory.credit_card_full(card_type='diners')), True)
        self.assertFalse(is_ccredito_diners(self.FakeFactory.credit_card_full(card_type='amex')))
        self.assertFalse(is_ccredito_diners(self.FakeFactory.credit_card_full(card_type='mastercard')))
        self.assertFalse(is_ccredito_diners(self.FakeFactory.credit_card_full(card_type='visa')))
        with self.assertRaisesRegex(TypeError, "required string"):
            is_ccredito_amex(4210582570068192)

    def test_is_ccredito_master(self):
        self.assertEqual(is_ccredito_master(self.FakeFactory.credit_card_full(card_type='mastercard')), True)
        self.assertFalse(is_ccredito_master(self.FakeFactory.credit_card_full(card_type='amex')))
        self.assertFalse(is_ccredito_master(self.FakeFactory.credit_card_full(card_type='diners')))
        self.assertFalse(is_ccredito_master(self.FakeFactory.credit_card_full(card_type='visa')))
        with self.assertRaisesRegex(TypeError, "required string"):
            is_ccredito_amex(4210582570068192)

    def test_is_ccredito_visa(self):
        self.assertEqual(is_ccredito_visa(self.FakeFactory.credit_card_full(card_type='visa')), True)
        self.assertFalse(is_ccredito_visa(self.FakeFactory.credit_card_full(card_type='amex')))
        self.assertFalse(is_ccredito_visa(self.FakeFactory.credit_card_full(card_type='diners')))
        self.assertFalse(is_ccredito_visa(self.FakeFactory.credit_card_full(card_type='mastercard')))
        with self.assertRaisesRegex(TypeError, "required string"):
            is_ccredito_amex(375854865070103)

    def test_isdate(self):
        def tile(s):
            result = []
            for x in s.split():
                if len(x) > 3:
                    result.append(x.title())
                else:
                    result.append(x)
            return ' '.join(result)
        for item in range(100):
            self.assertEqual(is_date(self.FakeFactory.date_this_year().strftime("%d/%m/%Y")), True)
            self.assertEqual(is_date(self.FakeFactory.date_this_year().strftime("%d.%m.%Y")), True)
            self.assertEqual(is_date(self.FakeFactory.date_this_century().strftime("%Y-%m-%d")), True)
            self.assertEqual(is_date(self.FakeFactory.date_this_century().strftime("%Y.%m.%d")), True)
            self.assertEqual(is_date(self.FakeFactory.date_this_century().strftime("%d de %B de %Y")), True)
            self.assertEqual(is_date(self.FakeFactory.date_this_century().strftime("%B %d, %Y").title()), True)
            self.assertEqual(is_date(tile(self.FakeFactory.date_this_century().strftime("%A, %d de %B de %Y."))), True)
        self.assertFalse(is_date('Januario 26, 2021'))
        self.assertFalse(is_date('Sexta, 30 de Fevereiro de 2008.'))
        self.assertFalse(is_date('Sexto, 03 de Outubro de 2008.'))
        self.assertFalse(is_date('Sexta, 03 de Outubo de 2008.'))
        self.assertFalse(is_date('30-2-2021'))

    def test_email(self):
        for i in range(100):
            self.assertEqual(True, isemail(self.FakeFactory.ascii_free_email()))
            self.assertEqual(True, isemail(self.FakeFactory.ascii_safe_email()))
            self.assertEqual(True, isemail(self.FakeFactory.ascii_company_email()))

    @unittest.skip(reason='implemented on pytest.')
    def test_fone(self):
        for i in range(100):
            result = self.FakeFactory.phone_number()
            self.assertEqual(True, isfone(result))

    def test_ipv4(self):
        for i in range(100):
            self.assertEqual(True, is_ipv4(self.FakeFactory.ipv4_private()))
            self.assertEqual(True, is_ipv4(self.FakeFactory.ipv4_public(network=False, address_class=None)))
            self.assertEqual(True, is_ipv4(self.FakeFactory.ipv4(network=False, address_class=None, private=None)))
            self.assertEqual(True, is_ipv4(self.FakeFactory.ipv4(network=False, address_class='a', private=None)))
            self.assertEqual(True, is_ipv4(self.FakeFactory.ipv4(network=False, address_class='b', private=None)))
            self.assertEqual(True, is_ipv4(self.FakeFactory.ipv4(network=False, address_class='c', private=None)))
            self.assertEqual(True, is_ipv4(self.FakeFactory.ipv4(network=False, address_class='a', private=True)))
            self.assertEqual(True, is_ipv4(self.FakeFactory.ipv4(network=False, address_class='b', private=True)))
            self.assertEqual(True, is_ipv4(self.FakeFactory.ipv4(network=False, address_class='c', private=True)))
        self.assertFalse(is_ipv4('256.158.155.13'))
        self.assertFalse(is_ipv4('255.158.155.256'))

    def test_ipv6(self):
        [self.assertEqual(True, is_ipv6(self.FakeFactory.ipv6(network=False))) for _ in range(100)]

    def test_url(self):
        for i in range(100):
            self.assertEqual(is_url(self.FakeFactory.url()), True)
            self.assertEqual(is_url(self.FakeFactory.uri()), True)
        self.assertTrue(is_url('ftp://unb.br'))
        self.assertTrue(is_url('ftps://unb.br/disc/arq.pdf'))
        self.assertTrue(is_url('http://localhost:8000'))
        self.assertTrue(is_url('http://127.0.0.1:3141/'))
        self.assertTrue(is_url('ftps://127.255.0.1:8234567'))
        self.assertTrue(is_url('https://incolume.com.br:443/universo/python'))
        self.assertTrue(is_url('ftp://8.8.8.8'))
        self.assertTrue(is_url('ftps://8.8.8.8'))
        self.assertTrue(is_url('http://8.8.8.8'))
        self.assertTrue(is_url('http://8.8.8.8:43'))
        self.assertTrue(is_url('https://8.8.8.8:43'))
        self.assertFalse(is_url('https://incolume.com.br:0/universo/python'))
        self.assertFalse(is_url('http:/incolume.com.br/py/dev'))
        self.assertFalse(is_url('https//incolume.com.br:443/universo/python'))
        self.assertFalse(is_url('casa'))
        self.assertFalse(is_url('casa.azul'))
        self.assertFalse(is_url('casa/'))

    @unittest.skip
    def test_url_1(self):
        # Valores inválidos
        self.assertFalse(is_url('ftp://257.255.255.255:82'))
        self.assertFalse(is_url('ftp://127.256.0.1:80'))
        self.assertFalse(is_url('ftp://127.255.256.1:80'))
        self.assertFalse(is_url('ftp://127.255.255.256:82'))


if __name__ == '__main__':
    unittest.main()
