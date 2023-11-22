#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  19: Proceder com as implementações necessárias para que passe nos testes

Instruções:

Baixe a versão mais recente do webdriver para seu sistema operacional em https://github.com/mozilla/geckodriver/tags

Descompacte-o em incolume/py/tdd/geckodrivers
Altere suas permisões para somente leitura

Em um terminal exclusivo, siga as etapas abaixo para ativar micro servidor web:
$ cd incolume/py/tdd/static_html/
$ python -m http.server

Mantenha este terminal ativo para realizar os testes necessários.
"""
import unittest
import urllib3
from pathlib import Path
import os
from incolume.py.tdd.scraping.python_org import PythonOrg, webdriver, platform

__author__ = '@britodfbr'


class NavegableSeleniumTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sitepy = Path(__file__).parent.parent.joinpath(
            'incolume', 'py', 'static_html', 'www.python.org', 'index.html'
        )
        self.atualdir = os.getcwd()
        self.serverdir = os.path.dirname(self.sitepy)
        self.instance = PythonOrg()
        self.url = 'http://127.0.0.1:8000/www.python.org/'

    def tearDown(self) -> None:
        pass
        self.instance.firefox.close()

    def test_server_http_is_active(self):
        """Verificar se servidor local está ativo"""
        req = urllib3.PoolManager()
        response = req.request('GET', self.url)
        if not response.status == 200:
            exit(1)
        self.assertEqual(response.status, 200)

    def test_filein_exists(self):
        assert os.path.isfile(self.sitepy), "Ops, {}".format(self.sitepy)

    def test_path(self):
        self.assertTrue(os.path.isdir, self.serverdir)
        self.assertEqual('www.python.org', self.serverdir.split('/')[-1])

    def test_ifdrivers(self):
        localbase = Path(__file__).parent.parent.joinpath('incolume','py', 'tdd', 'geckodrivers')
        local = ''
        if platform.system().lower() in ('linux', 'macos'):
            local = localbase / 'geckodriver'
        elif 'windows' == platform.system().lower():
            local = localbase / 'geckodriver.exe'

        assert os.path.isfile(local), "Driver indisponível: \"{}\"".format(local)
        self.assertTrue(local.is_file())

    @unittest.skip('activation future')
    def test_permitions(self):
        localbase = Path(__file__).parent.parent.joinpath('incolume','py', 'tdd', 'geckodrivers')
        local = localbase / 'geckodriver.exe' if platform.system().lower() == 'windows' else localbase / 'geckdriver'

        # Validação de permissões
        self.assertTrue(os.access(local, os.R_OK))    # Read
        self.assertTrue(os.access(local, os.X_OK))    # Excution
        self.assertFalse(os.access(local, os.W_OK))   # Write

    def test_Class(self):
        self.assertTrue(PythonOrg.__dict__)
        self.assertIn("pythonorg", PythonOrg.__dict__)

    def test_environment(self):
        self.assertIn('MOZ_HEADLESS', os.environ)
        self.assertEqual(os.environ['MOZ_HEADLESS'], '1')

    def test_firefox_desired_capabilities(self):
        self.assertIn('firefox_desired_capabilities', self.instance.__dict__)

    def test_current_url(self):
        expected = "http://127.0.0.1:8000/www.python.org/"
        self.assertEqual(expected, self.instance.index_current_url)

    def test_index_title_tagname(self):
        self.assertEqual(self.instance.index_title_tagname, "title")

    def test_index_page_content_type(self):
        self.assertIsInstance(self.instance.index_page_content, str)

    def test_index_page_content_length(self):
        self.assertGreaterEqual(len(self.instance.index_page_content), 47300)

    def test_index_page_content(self):
        self.assertTrue('0be1d290.js' in self.instance.index_page_content)

    def test_query_by_class_tier2_dict(self):
        """Esperado um dicionário com todos os links de class tier-2 """
        expected = "https://www.google.com/services/"
        result = self.instance.query_by_class_tier2_dict()
        self.assertIsInstance(result, dict)
        self.assertEqual(55, len(result))
        self.assertNotIn(' ', result.keys())
        self.assertNotIn('', result.keys())
        self.assertIn('All releases', result.keys())
        self.assertIn('https://mail.python.org/mailman/listinfo/python-dev', result.values())
        self.assertEqual(result['All releases'], 'http://127.0.0.1:8000/downloads/')
        self.assertEqual(result['PEP Index'], 'http://python.org/dev/peps/')
        self.assertIn(('Other Platforms', 'http://127.0.0.1:8000/download/other/'), result.items())

    def test_navegabilidade(self):
        """Capture o link contido em
        'Socialize > Chat on IRC > freenode's webchat' """
        expected = 'https://webchat.freenode.net/'
        result = self.instance.webchat_freenode()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
