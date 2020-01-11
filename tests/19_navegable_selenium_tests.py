#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Instruções:

Baixe o webdriver para seu sistema operacional em https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
Descompacte-o em incolumepy/geckodrivers
Altere suas permisões para somente leitura

Em um terminal exclusivo siga as etapas abaixo para ativar micro servidor web:
$ cd incolumepy/static_html/www.python.org
$ python -m http.server

"""
import unittest
import urllib3
from incolumepy.scraping.python_org import PythonOrg, webdriver, os, platform


class NavegableSeleniumTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sitepy = os.path.realpath(
            os.path.join(os.path.dirname(__file__), '..', 'incolumepy', 'static_html', 'www.python.org', 'index.html')
        )
        self.atualdir = os.getcwd()
        self.serverdir = os.path.dirname(self.sitepy)
        self.instance = PythonOrg()
        self.url = 'http://127.0.0.1:8000'

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
        localbase = os.path.relpath(os.path.join(os.path.dirname(__file__), '..', 'incolumepy', 'geckodrivers'))
        local = ''
        if platform.system().lower() in ('linux', 'macos'):
            local = os.path.join(localbase, 'geckodriver')
        elif 'windows' == platform.system().lower():
            local = os.path.join(localbase, 'geckodriver.exe')

        assert os.path.isfile(local), "Driver indisponível: \"{}\"".format(local)
        self.assertTrue(os.access(local, os.R_OK))
        self.assertTrue(os.access(local, os.X_OK))
        self.assertFalse(os.access(local, os.W_OK))

    def test_Class(self):
        self.assertTrue(PythonOrg.__dict__)
        self.assertIn("pythonorg", PythonOrg.__dict__)

    def test_environment(self):
        self.assertIn('MOZ_HEADLESS', os.environ)
        self.assertEqual(os.environ['MOZ_HEADLESS'], '1')

    def test_firefox_desired_capabilities(self):
        self.assertIn('firefox_desired_capabilities', self.instance.__dict__)

    def test_current_url(self):
        expected = "http://127.0.0.1:8000/"
        self.assertEqual(expected, self.instance.index_current_url)

    def test_index_title_tagname(self):
        self.assertEqual(self.instance.index_title_tagname, "title")

    def test_index_page_content(self):
        self.assertIsInstance(self.instance.index_page_content, str)
        self.assertEqual(50021, len(self.instance.index_page_content))
        self.assertEqual('0be1d290.js"', self.instance.index_page_content[-100:-88])

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
        """Capture o link contido em 'Socialize > Chat on IRC > freenode's webchat' """
        expected = 'https://webchat.freenode.net/'
        result = self.instance.webchat_freenode()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
