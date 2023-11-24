#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup, NavigableString


class GoogleSearch:
    def __init__(self, filein=''):
        self.filein = filein
        self._content = None
        self._soup = None
        self._html_attrs = None
        self._body_attrs = None
        self._query_href = None

    @property
    def soup(self):
        if not self._soup:
            self._soup = BeautifulSoup(self.content, 'html5lib')
        return self._soup

    @property
    def content(self):
        if not self._content:
            with open(self.filein) as f:
                self._content = f.read()
        return self._content

    @property
    def html_attrs(self):
        if not self._html_attrs:
            self._html_attrs = self.soup.html.attrs
        return self._html_attrs

    @property
    def body_attrs(self):
        if not self._body_attrs:
            self._body_attrs = self.soup.body.attrs
        return self._body_attrs

    def query_href(self, strbusca: str):
        return self.soup.find('a', string=re.compile(strbusca, re.I))['href']

    def form_inputs_name(self):
        q = self.soup.select('input[name]')
        return {'{}-{}'.format(r.name, r['name']): r.attrs for r in q}

    def form_principal_input_title(self) -> str:
        return self.soup.select('input[title]')[0]['title']
