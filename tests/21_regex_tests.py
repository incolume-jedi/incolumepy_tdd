"""# TODO: Atividade  21: Proceder com as implementações necessárias para
que passe nos testes.

Regras para identificar bandeira do cartão de crédito:
https://pastebin.com/CiKUtZRU
"""
__author__ = '@britodfbr'
import locale
import unittest
from itertools import chain

import pytest
import rstr
from faker import Factory
from faker.providers import date_time, internet
from incolume.py.tdd.utils.regex import (
    is_ccredito_amex,
    is_ccredito_diners,
    is_ccredito_master,
    is_ccredito_visa,
    is_date,
    is_ipv4,
    is_ipv6,
    is_url,
    isemail,
    isfone,
    re,
)


def fake_factory():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    FakeFactory = Factory.create('pt_BR')
    FakeFactory.add_provider(date_time)
    FakeFactory.add_provider(internet)
    return FakeFactory


class TestRegex:
    """Class TestRegex for 21_regex."""

    @pytest.mark.parametrize(
        'entrance',
        chain(
            [],
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
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        cls.FakeFactory = Factory.create('pt_BR')
        cls.FakeFactory.add_provider(date_time)
        cls.FakeFactory.add_provider(internet)

    def setUp(self) -> None:
        self.FakeFactory.credit_card_expire(
            start='now',
            end='+10y',
            date_format='%m/%y',
        )

    def re_validate(self):
        assert __file__ == re.match('tests')

    def test_is_ccredito_amex(self):
        assert (
            is_ccredito_amex(
                self.FakeFactory.credit_card_full(card_type='amex')
            )
            is True
        )
        assert not is_ccredito_amex(
            self.FakeFactory.credit_card_full(card_type='diners')
        )
        assert not is_ccredito_amex(
            self.FakeFactory.credit_card_full(card_type='mastercard')
        )
        assert not is_ccredito_amex(
            self.FakeFactory.credit_card_full(card_type='visa')
        )
        assert not is_ccredito_amex(
            'VISA 16 digit \nVinicius Novaes \n4210582570068192 07/28 \nCVC: 846'
        )
        with pytest.raises(TypeError, match='required string'):
            is_ccredito_amex(4210582570068192)

    def test_is_ccredito_diners(self):
        assert (
            is_ccredito_diners(
                self.FakeFactory.credit_card_full(card_type='diners')
            )
            is True
        )
        assert not is_ccredito_diners(
            self.FakeFactory.credit_card_full(card_type='amex')
        )
        assert not is_ccredito_diners(
            self.FakeFactory.credit_card_full(card_type='mastercard')
        )
        assert not is_ccredito_diners(
            self.FakeFactory.credit_card_full(card_type='visa')
        )
        with pytest.raises(TypeError, match='required string'):
            is_ccredito_amex(4210582570068192)

    def test_is_ccredito_master(self):
        assert (
            is_ccredito_master(
                self.FakeFactory.credit_card_full(card_type='mastercard')
            )
            is True
        )
        assert not is_ccredito_master(
            self.FakeFactory.credit_card_full(card_type='amex')
        )
        assert not is_ccredito_master(
            self.FakeFactory.credit_card_full(card_type='diners')
        )
        assert not is_ccredito_master(
            self.FakeFactory.credit_card_full(card_type='visa')
        )
        with pytest.raises(TypeError, match='required string'):
            is_ccredito_amex(4210582570068192)

    def test_is_ccredito_visa(self):
        assert (
            is_ccredito_visa(
                self.FakeFactory.credit_card_full(card_type='visa')
            )
            is True
        )
        assert not is_ccredito_visa(
            self.FakeFactory.credit_card_full(card_type='amex')
        )
        assert not is_ccredito_visa(
            self.FakeFactory.credit_card_full(card_type='diners')
        )
        assert not is_ccredito_visa(
            self.FakeFactory.credit_card_full(card_type='mastercard')
        )
        with pytest.raises(TypeError, match='required string'):
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
            assert (
                is_date(self.FakeFactory.date_this_year().strftime('%d/%m/%Y'))
                is True
            )
            assert (
                is_date(self.FakeFactory.date_this_year().strftime('%d.%m.%Y'))
                is True
            )
            assert (
                is_date(
                    self.FakeFactory.date_this_century().strftime('%Y-%m-%d')
                )
                is True
            )
            assert (
                is_date(
                    self.FakeFactory.date_this_century().strftime('%Y.%m.%d')
                )
                is True
            )
            assert (
                is_date(
                    self.FakeFactory.date_this_century().strftime(
                        '%d de %B de %Y'
                    )
                )
                is True
            )
            assert (
                is_date(
                    self.FakeFactory.date_this_century()
                    .strftime('%B %d, %Y')
                    .title()
                )
                is True
            )
            assert (
                is_date(
                    tile(
                        self.FakeFactory.date_this_century().strftime(
                            '%A, %d de %B de %Y.'
                        )
                    )
                )
                is True
            )
        assert not is_date('Januario 26, 2021')
        assert not is_date('Sexta, 30 de Fevereiro de 2008.')
        assert not is_date('Sexto, 03 de Outubro de 2008.')
        assert not is_date('Sexta, 03 de Outubo de 2008.')
        assert not is_date('30-2-2021')

    def test_email(self):
        for i in range(100):
            assert True is isemail(self.FakeFactory.ascii_free_email())
            assert True is isemail(self.FakeFactory.ascii_safe_email())
            assert True is isemail(self.FakeFactory.ascii_company_email())

    @unittest.skip(reason='implemented on pytest.')
    def test_fone(self):
        for i in range(100):
            result = self.FakeFactory.phone_number()
            assert True is isfone(result)

    def test_ipv4(self):
        for i in range(100):
            assert True is is_ipv4(self.FakeFactory.ipv4_private())
            assert True is is_ipv4(
                self.FakeFactory.ipv4_public(network=False, address_class=None)
            )
            assert True is is_ipv4(
                self.FakeFactory.ipv4(
                    network=False, address_class=None, private=None
                )
            )
            assert True is is_ipv4(
                self.FakeFactory.ipv4(
                    network=False, address_class='a', private=None
                )
            )
            assert True is is_ipv4(
                self.FakeFactory.ipv4(
                    network=False, address_class='b', private=None
                )
            )
            assert True is is_ipv4(
                self.FakeFactory.ipv4(
                    network=False, address_class='c', private=None
                )
            )
            assert True is is_ipv4(
                self.FakeFactory.ipv4(
                    network=False, address_class='a', private=True
                )
            )
            assert True is is_ipv4(
                self.FakeFactory.ipv4(
                    network=False, address_class='b', private=True
                )
            )
            assert True is is_ipv4(
                self.FakeFactory.ipv4(
                    network=False, address_class='c', private=True
                )
            )
        assert not is_ipv4('256.158.155.13')
        assert not is_ipv4('255.158.155.256')

    def test_ipv6(self):
        [
            self.assertEqual(
                True,
                is_ipv6(self.FakeFactory.ipv6(network=False)),
            )
            for _ in range(100)
        ]

    def test_url(self):
        for i in range(100):
            assert is_url(self.FakeFactory.url()) is True
            assert is_url(self.FakeFactory.uri()) is True
        assert is_url('ftp://unb.br')
        assert is_url('ftps://unb.br/disc/arq.pdf')
        assert is_url('http://localhost:8000')
        assert is_url('http://127.0.0.1:3141/')
        assert is_url('ftps://127.255.0.1:8234567')
        assert is_url('https://incolume.com.br:443/universo/python')
        assert is_url('ftp://8.8.8.8')
        assert is_url('ftps://8.8.8.8')
        assert is_url('http://8.8.8.8')
        assert is_url('http://8.8.8.8:43')
        assert is_url('https://8.8.8.8:43')
        assert not is_url('https://incolume.com.br:0/universo/python')
        assert not is_url('http:/incolume.com.br/py/dev')
        assert not is_url('https//incolume.com.br:443/universo/python')
        assert not is_url('casa')
        assert not is_url('casa.azul')
        assert not is_url('casa/')

    @unittest.skip
    def test_url_1(self):
        # Valores inválidos
        assert not is_url('ftp://257.255.255.255:82')
        assert not is_url('ftp://127.256.0.1:80')
        assert not is_url('ftp://127.255.256.1:80')
        assert not is_url('ftp://127.255.255.256:82')


if __name__ == '__main__':
    unittest.main()
