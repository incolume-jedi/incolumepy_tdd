#!/usr/bin/env python
"""# TODO: Atividade  20: Proceder com as implementações necessárias para que passe nos testes.

Utilize o pacote requests para acessar a lei 8666/1993 no webcache do projeto
referente a 2019, disponível em
http://localhost:8000/legis.senado.leg.br/norma/527942/publicacao/15718520.html
salve o texto original com o nome
"incolume/py/tdd/scraping/artefacts/atos/l8666-txtSF.html";
mantenha o texto original sem alterações!
Transforme em HTML5, aplique o CSS disponível em
"incolume/py/static_html/css/legis_3.css",
formate o cabeçalho (head, h1, h2, h3), aplique as
classes presidente, ministro, data e dou.
arquivo final com todas as alterações deverá estar em
"incolume/tdd/scraping/artefacts/atos/L8666.html".

OBS: Para proceder com este exercício o ambiente deve ser configurado como descrito em
00_environment_tests.py; o http.server deve permanecer ativo para realizar este exercício.
"""
__author__ = '@britodfbr'
import hashlib
import os
import re
import shutil
import tempfile
import time
import unittest
from collections import namedtuple
from pathlib import Path
from unittest import mock

from incolume.py.tdd.scraping.htmlformating import (
    formating,
    get_content,
    gravar,
    identify_recover,
    output,
    outputdir,
    partial,
    req_lei8666,
    requests,
    save_content,
)

from tests import has_internet


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, content, status_code) -> None:
            self.content = content
            self.status_code = status_code

        def json(self):
            return self.content

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({'key1': 'value1'}, 200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({'key2': 'value2'}, 200)

    return MockResponse(None, 404)


# @unittest.skip(reason="Not run yet")
class HandleHTMLTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://localhost:8000/legis.senado.leg.br/norma/527942/publicacao/15718520.html'
        cls.req = req_lei8666(cls.url) if has_internet() else None
        cls.tmp = tempfile.gettempdir()

    def setUp(self) -> None:
        self.filebase = (
            Path(__file__)
            .parents[1]
            .joinpath('incolume', 'py', 'tdd', 'scraping', 'artefacts', 'atos')
        )
        self.filename = lambda: Path(self.tmp).joinpath(
            Path(__file__).stem,
            f'{time.time():.0f}.txt',
        )

    def tearDown(self) -> None:
        """Desmontagem do método."""
        shutil.rmtree(os.path.dirname(self.filename()), ignore_errors=True)
        [x.unlink() for x in self.filebase.glob('*.html')]

    @classmethod
    def tearDownClass(cls) -> None:
        """Desmontagem da classe."""
        del cls.url
        del cls.req
        del cls.tmp

    def test_packages_variables(self):
        assert isinstance(output, (str, Path))
        assert isinstance(outputdir, (str, Path))

    @unittest.skipUnless(has_internet(), reason='Requer Internet')
    def test_resquest_http_response(self):
        assert isinstance(self.req, requests.models.Response)

    @unittest.skipUnless(has_internet(), reason='Requer Internet')
    def test_resquest_http_status_code(self):
        assert self.req.status_code == 200

    def test_gravar_output_name(self):
        filename = self.filename().as_posix()
        assert re.search('.*20_handle_html_tests.\\d{10}.txt', filename)

    def test_gravar(self):
        filename = self.filename()
        assert gravar.__annotations__ == {
            'code': (str, bytes),
            'filename': str,
            'mode': str,
            'return': bool,
        }
        conteudo = 'conteúdo de teste\n'
        assert gravar(conteudo, filename)
        with open(filename) as f:
            assert f.read() == conteudo

        conteudo = b'conte\xc3\xbado de teste\n'
        assert gravar(conteudo, filename)
        with open(filename, 'rb') as f:
            assert f.read() == conteudo

    @unittest.skipUnless(has_internet(), reason='Requer Internet')
    def test_content(self):
        assert get_content(self.url) is not None

    def test_content_offline(self):
        with mock.patch(
            'incolume.py.tdd.scraping.htmlformating.requests.get',
        ) as m:
            mock_req_get = namedtuple('Mock', 'content status_code')
            mock_req_get.content = self.filebase.joinpath('l8666-txtSF.html')
            m.return_value = mock_req_get
            assert get_content(self.url) is not None

    @unittest.skipUnless(has_internet(), 'Requer Internet')
    def test_get_content(self):
        """test_get_content:"""
        assert get_content(self.url) == self.req.content

    @unittest.skip(reason='implementação futura')
    def test_get_content_offline(self):
        """test_get_content:"""
        with mock.patch(
            'incolume.py.tdd.scraping.htmlformating.requests.get',
        ) as m:
            mock_req_get = namedtuple('Mock', 'content status_code')
            mock_req_get.status_code = 200
            mock_req_get.content = self.filebase.joinpath(
                'l8666-txtSF.html',
            ).read_bytes()
            m.return_value = mock_req_get
            content = save_content(get_content(self.url))
            assert content == self.req.content

    @unittest.skipUnless(has_internet(), reason='Requer Internet')
    def test_save(self):
        """test_save_content:
        Válida a implementação do metodo save_content e a gravação do conteudo no local correto.
        """
        output_esperada = self.filebase.joinpath('l8666-txtSF.html')

        assert isinstance(save_content, partial)
        with mock.patch('builtins.open', create=False) as mock_open:
            save_content('html text')
            assert mock.call(output_esperada, 'w') == mock_open.call_args
            assert mock_open.called

    @unittest.skip(
        reason='TypeError: in str which requires string as left operand, not MagicMock',
    )
    @unittest.skipUnless(has_internet(), reason='Requer Internet')
    def test_save_content(self):
        output_esperada = self.filebase.joinpath('l8666-txtSF.html')
        with mock.patch('builtins.open', create=False) as mock_open:
            save_content(get_content(self.url))
            assert mock.call(output_esperada, 'wb') == mock_open.call_args
            assert mock_open.called

    @unittest.skipUnless(has_internet(), reason='Requer Internet')
    def test_save_content1(self):
        output_esperada = self.filebase.joinpath('l8666-txtSF.html')
        save_content(get_content(self.url))
        assert os.path.isfile(output_esperada), f'Ops: {output_esperada}'
        output_esperada.unlink()

    def test_text_identify_recover(self):
        """test_text_identify_recover: Valida a Gravação em outro arquivo somente o conteúdo principal um HTML puro de texto
        limpo.
        """
        save_content(get_content(self.url))
        filein = self.filebase.joinpath('l8666-txtSF.html')
        assert os.path.isfile(filein), f'Ops: {filein}'
        fileout = self.filebase.joinpath('L8666.html')

        assert identify_recover.__annotations__ == {
            'pathfile': str,
            'return': str,
        }
        result = identify_recover(filein)
        assert isinstance(result, bytes)
        assert len(result) == 168065
        assert os.path.isfile(fileout)

        sha1 = hashlib.sha1()
        sha1.update(result)
        assert (
            sha1.hexdigest() == '79a42e4056b56d1a2e8528cb0274a0415361db4f'
        ), 'Ops: Arquivo diverge do esperado. Limpe-o completamente!'

    def test_formating(self):
        """Converter para HTML5, em ascii puro, aplicar CSS legis_03.css ao l8666.html,
         inserir cabeçalho no topo do body
        <header>
          <h1> Presidência da República</h1> <h2>Secretaria Geral</h2> <h3>Subchefia para Assuntos Jurídicos</h3>
        </header>
        Aplicar classes CSS (epigrafe, ementa, presidente, ministro (a cada ministro), dou) ao documento
        e salvar o resultado em static_html/atos/L8666.html.
        """
        filein = self.filebase.joinpath('l8666-txtSF.html')
        save_content(get_content(self.url))
        identify_recover(filein)

        pathfile = self.filebase.joinpath('L8666.html')
        assert os.path.isfile(pathfile), f'Ops: {pathfile}'
        output = self.filebase.joinpath('L8666.html')

        assert formating.__annotations__ == {'pathfile': str, 'return': str}
        result = formating(pathfile)
        assert isinstance(result, bytes)
        assert len(result) == 168482
        assert os.path.isfile(output)
        sha1 = hashlib.sha1()
        sha1.update(result)
        # print(sha1.hexdigest())
        assert (
            sha1.hexdigest() == '12896a793d2a5cb311ebb23363bf0bebbd3ca522'
        ), 'Ops: Arquivo diverge do esperado. Formate-o completamente!'


if __name__ == '__main__':
    unittest.main()
