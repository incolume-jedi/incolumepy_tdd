#!/usr/bin/env python
"""# TODO: Atividade  18: Manipulação em arquivo HTML.

Proceder com as implementações necessárias para que passe nos testes

OBS: Para proceder com este exercício o ambiente deve ser configurado como descrito em
00_environment_tests.py; o http.server deve permanecer ativo para realizar este exercício.
"""
__author__ = '@britodfbr'
import os
import unittest
from pathlib import Path

import pytest
from incolume.py.tdd.scraping.google import (
    BeautifulSoup,
    GoogleSearch,
    NavigableString,
)


class ScrapingHTMLTest(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(
            Path(__file__).parent.parent.joinpath(
                'incolume', 'py', 'static_html', 'google.com', 'index.html',
            ),
        )
        self.google_search = GoogleSearch(self.path)

    def test_instance(self):
        assert isinstance(GoogleSearch, object)
        assert isinstance(self.google_search, GoogleSearch)
        assert self.google_search.__init__
        assert self.google_search.__repr__
        assert self.google_search.__dict__

    def test_filein(self):
        assert 'filein' in self.google_search.__dict__

    def test_filein_exists(self):
        assert os.path.exists(self.google_search.filein)
        assert os.path.realpath(self.path) == os.path.realpath(self.google_search.filein)

    def test_content(self):
        assert self.google_search.content
        assert '_content' in self.google_search.__dict__
        assert isinstance(self.google_search.content, str)
        assert 'Google treinamento Incólume' in self.google_search.content

        with pytest.raises(AttributeError, match="can't set attribute"):
            self.google_search.content = ''

    def test_soup(self):
        assert self.google_search.soup
        assert '_soup' in self.google_search.__dict__
        assert isinstance(self.google_search.soup, BeautifulSoup)
        assert self.google_search.soup.title.text == 'Google treinamento Incólume'

        with pytest.raises(AttributeError, match="can't set attribute"):
            self.google_search.soup = BeautifulSoup('', 'html.parser')

    def test_html_attrs(self):
        """Atributos da tag HTML."""
        expected = {
            'itemscope': '',
            'itemtype': 'http://schema.org/WebPage',
            'lang': 'pt-BR',
        }
        assert type(self.google_search.html_attrs), NavigableString
        assert self.google_search.html_attrs == expected

    def test_body_attrs(self):
        """Atributos da tag body."""
        expected = {'bgcolor': '#fff'}
        assert type(self.google_search.body_attrs), NavigableString
        assert self.google_search.body_attrs == expected

    def test_query_href_services(self):
        """Href de Soluções empresariais."""
        entrance = 'Soluções empresariais'
        expected = 'https://www.google.com/services/'
        assert expected == self.google_search.query_href(entrance)

    def test_query_href_language(self):
        """Href de Ferramentas de idioma."""
        entrance = 'Ferramentas de idioma'
        expected = 'https://www.google.com/language_tools?hl=pt-BR&authuser=0'
        assert expected == self.google_search.query_href(entrance)

    def test_name_form_input(self):
        """Name do campo form.input de todos os elementos input no
        formato:
        tagname-tagattrname: {attrs}
        exemplo:
        'input-hl': {'name': 'hl', 'type': 'hidden', 'value': 'pt-BR'}.
        """
        expected = 7
        assert expected == len(self.google_search.form_inputs_name())

        expecteds = [
            'input-hl',
            'input-source',
            'input-q',
            'input-btnG',
            'input-btnI',
            'input-iflsig',
            'input-gbv',
        ]
        for expected in expecteds:
            assert expected in self.google_search.form_inputs_name()

    def test_title_form_input(self):
        """Title do campo form.input."""
        expected = 'Pesquisa Google'
        assert expected == self.google_search.form_principal_input_title()


if __name__ == '__main__':
    unittest.main()
