"""# TODO: Atividade  19: Selenium

Proceder com as implementações necessárias para que passe nos testes.

OBS: Para proceder com este exercício o ambiente deve ser configurado
como descrito em 00_environment_tests.py

o http.server deve permanecer ativo para realizar este exercício.
"""
import os
import sys
import unittest
from pathlib import Path

import urllib3
from incolume.py.tdd.scraping.python_org import PythonOrg, platform

__author__ = '@britodfbr'


class NavegableSeleniumTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sitepy = Path(__file__).parent.parent.joinpath(
            'incolume',
            'py',
            'static_html',
            'www.python.org',
            'index.html',
        )
        self.atualdir = os.getcwd()
        self.serverdir = os.path.dirname(self.sitepy)
        self.instance = PythonOrg()
        self.url = 'http://127.0.0.1:8000/www.python.org/'

    def tearDown(self) -> None:
        self.instance.firefox.close()

    def test_server_http_is_active(self):
        """Verificar se servidor local está ativo."""
        req = urllib3.PoolManager()
        response = req.request('GET', self.url)
        if response.status != 200:
            sys.exit(1)
        assert response.status == 200

    def test_filein_exists(self):
        assert os.path.isfile(self.sitepy), f'Ops, {self.sitepy}'

    def test_path(self):
        assert os.path.isdir, self.serverdir
        assert self.serverdir.split('/')[-1] == 'www.python.org'

    def test_ifdrivers(self):
        localbase = Path(__file__).parent.parent.joinpath(
            'incolume',
            'py',
            'tdd',
            'geckodrivers',
        )
        local = ''
        if platform.system().lower() in {'linux', 'macos'}:
            local = localbase / 'geckodriver'
        elif platform.system().lower() == 'windows':
            local = localbase / 'geckodriver.exe'

        assert os.path.isfile(local), f'Driver indisponível: "{local}"'
        assert local.is_file()

    @unittest.skip('activation future')
    def test_permitions(self):
        localbase = Path(__file__).parent.parent.joinpath(
            'incolume',
            'py',
            'tdd',
            'geckodrivers',
        )
        local = (
            localbase / 'geckodriver.exe'
            if platform.system().lower() == 'windows'
            else localbase / 'geckdriver'
        )

        # Validação de permissões
        assert os.access(local, os.R_OK)    # Read
        assert os.access(local, os.X_OK)    # Excution
        assert not os.access(local, os.W_OK)   # Write

    def test_Class(self):
        assert PythonOrg.__dict__
        assert 'pythonorg' in PythonOrg.__dict__

    def test_environment(self):
        assert 'MOZ_HEADLESS' in os.environ
        assert os.environ['MOZ_HEADLESS'] == '1'

    def test_firefox_desired_capabilities(self):
        assert 'firefox_desired_capabilities' in self.instance.__dict__

    def test_current_url(self):
        expected = 'http://127.0.0.1:8000/www.python.org/'
        assert expected == self.instance.index_current_url

    def test_index_title_tagname(self):
        assert self.instance.index_title_tagname == 'title'

    def test_index_page_content_type(self):
        assert isinstance(self.instance.index_page_content, str)

    def test_index_page_content_length(self):
        assert len(self.instance.index_page_content) >= 47300

    def test_index_page_content(self):
        assert '0be1d290.js' in self.instance.index_page_content

    def test_query_by_class_tier2_dict(self):
        """Esperado um dicionário com todos os links de class tier-2."""
        result = self.instance.query_by_class_tier2_dict()
        assert isinstance(result, dict)
        assert len(result) == 55
        assert ' ' not in result
        assert '' not in result
        assert 'All releases' in result
        assert (
            'https://mail.python.org/mailman/listinfo/python-dev'
            in result.values()
        )
        assert result['All releases'] == 'http://127.0.0.1:8000/downloads/'
        assert result['PEP Index'] == 'http://python.org/dev/peps/'
        assert (
            'Other Platforms',
            'http://127.0.0.1:8000/download/other/',
        ) in result.items()

    def test_navegabilidade(self):
        """Capture o link contido em
        'Socialize > Chat on IRC > freenode's webchat'.
        """
        expected = 'https://webchat.freenode.net/'
        result = self.instance.webchat_freenode()
        assert expected == result


if __name__ == '__main__':
    unittest.main()
