#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup, Comment, Doctype
import pathlib
import re
import requests

__author__ = '@britodfbr'
outputdir = pathlib.Path(__file__).parent.parent.joinpath('scraping', 'atos')
output = outputdir / 'L2848_1940.html'


class FormatingSF:
    def __init__(self, url):
        self.url = (
            url
            or 'https://legis.senado.leg.br/norma/527942/publicacao/15636360'
        )
        self.req = requests.get(url) or None

    def gravar(self):
        ...

    def get_content(self):
        return self.req.content

    def formating(self):
        ...
