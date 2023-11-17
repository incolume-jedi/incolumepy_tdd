import unittest
import locale
from faker import Factory
from faker.providers import internet
from faker.providers import date_time
from src.incolumepy.tdd.utils.regex import re
from src.incolumepy.tdd.utils.regex import is_ccredito_amex
from src.incolumepy.tdd.utils.regex import is_ccredito_diners
from src.incolumepy.tdd.utils.regex import is_ccredito_master
from src.incolumepy.tdd.utils.regex import is_ccredito_visa
from src.incolumepy.tdd.utils.regex import isdate
from src.incolumepy.tdd.utils.regex import isemail
from src.incolumepy.tdd.utils.regex import isfone
from src.incolumepy.tdd.utils.regex import isip
from src.incolumepy.tdd.utils.regex import isurl

# TODO: Atividade  21: Proceder com as implementações necessárias para que passe nos testes


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
        with self.assertRaisesRegex(TypeError, "required string"):
            is_ccredito_amex(4210582570068192)
        with self.assertRaises(ValueError):
            is_ccredito_amex("VISA 16 digit \nVinicius Novaes \n4210582570068192 07/28 \nCVC: 846")

    def test_is_ccredito_diners(self):
        self.assertEqual(is_ccredito_diners(self.FakeFactory.credit_card_full(card_type='diners')), True)
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='amex')))
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='mastercard')))
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='visa')))
        with self.assertRaisesRegex(TypeError, "required string"):
            is_ccredito_amex(4210582570068192)
        with self.assertRaises(ValueError):
            "American Express \nKaique Teixeira \n375854865070103 06/28 \nCID: 8086"

    def test_is_ccredito_master(self):
        self.assertEqual(is_ccredito_master(self.FakeFactory.credit_card_full(card_type='mastercard')), True)
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='diners')))
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='mastercard')))
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='visa')))
        with self.assertRaisesRegex(TypeError, "required string"):
            is_ccredito_amex(4210582570068192)
        with self.assertRaises(ValueError):
            "American Express \nKaique Teixeira \n375854865070103 06/28 \nCID: 8086"

    def test_is_ccredito_visa(self):
        self.assertEqual(is_ccredito_visa(self.FakeFactory.credit_card_full(card_type='visa')), True)
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='amex')))
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='diners')))
        self.assertFalse(is_ccredito_amex(self.FakeFactory.credit_card_full(card_type='mastercard')))
        with self.assertRaisesRegex(TypeError, "required string"):
            is_ccredito_amex(375854865070103)
        with self.assertRaises(ValueError):
            "American Express \nKaique Teixeira \n375854865070103 06/28 \nCID: 8086"

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
            self.assertEqual(isdate(self.FakeFactory.date_this_year().strftime("%d/%m/%Y")), True)
            self.assertEqual(isdate(self.FakeFactory.date_this_year().strftime("%d.%m.%Y")), True)
            self.assertEqual(isdate(self.FakeFactory.date_this_century().strftime("%Y-%m-%d")), True)
            self.assertEqual(isdate(self.FakeFactory.date_this_century().strftime("%Y.%m.%d")), True)
            self.assertEqual(isdate(self.FakeFactory.date_this_century().strftime("%d de %B de %Y")), True)
            self.assertEqual(isdate(self.FakeFactory.date_this_century().strftime("%B %d, %Y").title()), True)
            self.assertEqual(isdate(tile(self.FakeFactory.date_this_century().strftime("%A, %d de %B de %Y."))), True)

    def test_email(self):
        for i in range(100):
            self.assertEqual(True, isemail(self.FakeFactory.ascii_free_email()))
            self.assertEqual(True, isemail(self.FakeFactory.ascii_safe_email()))
            self.assertEqual(True, isemail(self.FakeFactory.ascii_company_email()))

    def test_fone(self):
        for i in range(100):
            self.assertEqual(True, isfone(self.FakeFactory.phone_number()))

    def test_ip(self):
        for i in range(100):
            self.assertEqual(True, isip(self.FakeFactory.ipv4_private()))
            self.assertEqual(True, isip(self.FakeFactory.ipv4_public(network=False, address_class=None)))
            self.assertEqual(True, isip(self.FakeFactory.ipv4(network=False, address_class=None, private=None)))
            self.assertEqual(True, isip(self.FakeFactory.ipv4(network=False, address_class='a', private=None)))
            self.assertEqual(True, isip(self.FakeFactory.ipv4(network=False, address_class='b', private=None)))
            self.assertEqual(True, isip(self.FakeFactory.ipv4(network=False, address_class='c', private=None)))
            self.assertEqual(True, isip(self.FakeFactory.ipv4(network=False, address_class='a', private=True)))
            self.assertEqual(True, isip(self.FakeFactory.ipv4(network=False, address_class='b', private=True)))
            self.assertEqual(True, isip(self.FakeFactory.ipv4(network=False, address_class='c', private=True)))
            self.assertEqual(True, isip(self.FakeFactory.ipv6(network=False)))
        self.assertFalse(isip('256.158.155.13'))
        self.assertFalse(isip('255.158.155.256'))

    def test_url(self):
        for i in range(100):
            self.assertEqual(isurl(self.FakeFactory.url()), True)
            self.assertEqual(isurl(self.FakeFactory.uri()), True)
        self.assertTrue(isurl('ftp://unb.br'))
        self.assertTrue(isurl('ftps://unb.br/disc/arq.pdf'))
        self.assertTrue(isurl('http://localhost:8000'))
        self.assertTrue(isurl('http://127.0.0.1:3141/'))
        self.assertTrue(isurl('https://incolume.com.br:443/universo/python'))
        self.assertFalse(isurl('http:/incolume.com.br/py/dev'))
        self.assertFalse(isurl('casa'))
        self.assertFalse(isurl('casa.azul'))
        self.assertFalse(isurl('casa/'))


if __name__ == '__main__':
    unittest.main()
