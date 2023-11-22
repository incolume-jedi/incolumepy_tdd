import requests
import pytest
import sys
from pathlib import Path

""" # TODO: Atividade  : Proceder com as implementações necessárias para que passe nos testes

Instruções:
    Para Micro servidor web local:
    1. Em um terminal exclusivo, siga as etapas abaixo para ativar micro servidor web:
      $ cd incolume/py/tdd/static_html/
      $ python -m http.server 8000
    
    2. Mantenha este terminal ativo para realizar os testes.

    Para plugin Geckodrive:
    1. Baixe a versão mais recente do webdriver para seu sistema 
    operacional em https://github.com/mozilla/geckodriver/tags

    2. Descompacte-o em incolume/py/tdd/geckodrivers
    3. Altere suas permisões para somente leitura
"""

class TestMicroWebServer:
    """Test micro webserver ativate."""

    @pytest.mark.parametrize(
        'entrance',
        [
            'localhost',
            '127.0.0.1',
        ],
    )
    def test_local_server_http_is_active(self, entrance) -> None:
        """Test if local server HTTP is active."""
        result = requests.get(f'http://{entrance}:8000/')
        assert result.status_code == 200

    @pytest.mark.parametrize(
        'entrance',
        [
            ('localhost', 'google.com'),
            ('localhost', 'css/legis_3.css'),
            ('localhost', 'legis.senado.leg.br'),
            ('localhost', 'www.python.org'),
            ('127.0.0.1', 'google.com'),
            ('127.0.0.1', 'css/legis_3.css'),
            ('127.0.0.1', 'legis.senado.leg.br'),
            ('127.0.0.1', 'www.python.org'),
        ],
    )
    def test_local_server_http_directories(self, entrance) -> None:
        """Test if local server http has correct directories."""
        url = 'http://{}/{}/'.format(*entrance)
        result = requests.get(url)
        assert result.status_code == 200


class TestPluginGeckoDriver:
    """Test geckodriver exists."""

    @pytest.fixture()
    def driver_dir(self) -> Path:
        """Driver directory."""
        return Path(__file__).parents[1].joinpath('incolume','py', 'tdd', 'geckodrivers')

    @pytest.mark.skipif(sys.platform.startswith('win'), reason='Not available on windows.',)
    def test_has_plugin_unix_like(self, driver_dir) -> None:
        """Test if has plugin geckocriver."""
        driver = driver_dir / 'geckodriver'
        assert driver.is_file(), f"Driver indisponível: \"{driver}\""

    @pytest.mark.skipif(sys.platform.startswith('lin'), reason='Not available on Unix-like.',)
    @pytest.mark.skipif(sys.platform.startswith('mac'), reason='Not available on Unix-like.',)
    def test_has_plugin_win_like(self, driver_dir) -> None:
        """Test if has plugin geckocriver."""
        driver = driver_dir / 'geckodriver.exe'
        assert driver.is_file(), f"Driver indisponível: \"{driver}\""