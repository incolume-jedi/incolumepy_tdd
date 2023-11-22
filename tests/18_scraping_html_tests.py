#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  18: Manipulação em arquivo HTML.

Proceder com as implementações necessárias para que passe nos testes

"""
__author__ = '@britodfbr'
import unittest
import os
from pathlib import Path
from incolumepy.tdd.scraping.google import (
    GoogleSearch, BeautifulSoup, NavigableString,
)


class ScrapingHTMLTest(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(
            Path(__file__).parent.parent.joinpath(
                'incolumepy', 'static_html', 'google.com', 'index.html')
        )
        self.google_search = GoogleSearch(self.path)

    def test_instance(self):
        self.assertTrue(isinstance(GoogleSearch, object))
        self.assertTrue(isinstance(self.google_search, GoogleSearch))
        self.assertTrue(self.google_search.__init__)
        self.assertTrue(self.google_search.__repr__)
        self.assertTrue(self.google_search.__dict__)

    def test_filein(self):
        self.assertIn('filein', self.google_search.__dict__)

    def test_filein_exists(self):
        self.assertTrue(os.path.exists(self.google_search.filein))
        self.assertEqual(os.path.realpath(self.path),
                         os.path.realpath(self.google_search.filein))

    def test_content(self):
        self.assertTrue(self.google_search.content)
        self.assertIn('_content', self.google_search.__dict__)
        self.assertIsInstance(self.google_search.content, str)
        self.assertIn('Google treinamento Incólume',
                      self.google_search.content)

        with self.assertRaisesRegex(AttributeError,
                                    "can't set attribute"):
            self.google_search.content = ''

    def test_soup(self):
        self.assertTrue(self.google_search.soup)
        self.assertIn('_soup', self.google_search.__dict__)
        self.assertIsInstance(self.google_search.soup, BeautifulSoup)
        self.assertEqual('Google treinamento Incólume',
                         self.google_search.soup.title.text)

        with self.assertRaisesRegex(
            AttributeError,"can't set attribute"):
            self.google_search.soup = BeautifulSoup('',
                                                    'html.parser')

    def test_html_attrs(self):
        """Atributos da tag HTML"""
        expected = {'itemscope': '',
                    'itemtype': 'http://schema.org/WebPage', 'lang': 'pt-BR'}
        self.assertTrue(type(self.google_search.html_attrs), NavigableString)
        self.assertEqual(self.google_search.html_attrs, expected)

    def test_body_attrs(self):
        """Atributos da tag body"""
        expected = {'bgcolor': '#fff'}
        self.assertTrue(type(self.google_search.body_attrs), NavigableString)
        self.assertEqual(self.google_search.body_attrs, expected)

    def test_query_href_services(self):
        """href de Soluções empresariais """
        entrance = "Soluções empresariais"
        expected = "https://www.google.com/services/"
        self.assertEqual(expected, self.google_search.query_href(entrance))

    def test_query_href_language(self):
        """href de Ferramentas de idioma"""
        entrance = "Ferramentas de idioma"
        expected = "https://www.google.com/language_tools?hl=pt-BR&authuser=0"
        self.assertEqual(expected, self.google_search.query_href(entrance))

    def test_name_form_input(self):
        """Name do campo form.input de todos os elementos input no
        formato:
        tagname-tagattrname: {attrs}
        exemplo:
        'input-hl': {'name': 'hl', 'type': 'hidden', 'value': 'pt-BR'}
        """
        expected = 7
        self.assertEqual(expected, len(self.google_search.form_inputs_name()))

        expecteds = [
            'input-hl', 'input-source', 'input-q', 'input-btnG',
            'input-btnI', 'input-iflsig', 'input-gbv',
        ]
        for expected in expecteds:
            self.assertIn(expected,
                          self.google_search.form_inputs_name().keys())

    def test_title_form_input(self):
        """Title do campo form.input"""
        expected = 'Pesquisa Google'
        self.assertEqual(expected,
                         self.google_search.form_principal_input_title())


if __name__ == '__main__':
    unittest.main()
