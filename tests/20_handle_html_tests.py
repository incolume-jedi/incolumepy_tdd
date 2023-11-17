#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Atenda o que é requerido no TDD e inície Criando um metodo e Utilize o requests para acessar a
lei 8666/1993 em http://legis.senado.leg.br/norma/550542/publicacao/15718520,
que retorne a requisição http;


arquivo final com o nome incolume/static_html/atos/l8666.html.
"""

import unittest
import tempfile
import time
import shutil
import mock
import hashlib
import inspect
from src.incolumepy.scraping.htmlformating import (
    formating, requests, req_lei8666, get_content, gravar, os, save_content, partial, identify_recover
)


class HandleHTMLTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = "http://legis.senado.leg.br/norma/550542/publicacao/15718520"
        cls.req = req_lei8666(cls.url)
        cls.tmp = tempfile.gettempdir()

    def setUp(self) -> None:
        self.filename = lambda: \
            os.path.join(self.tmp, os.path.basename(__file__).split('.')[0], f"{int(time.time())}.txt")

    def tearDown(self) -> None:
        shutil.rmtree(os.path.dirname(self.filename()), ignore_errors=True)

    def test_resquest_http(self):
        self.assertIsInstance(self.req, requests.models.Response)
        self.assertEqual(self.req.status_code, 200)

    def test_gravar(self):
        filename = self.filename()
        self.assertRegex(filename, r'/tmp/20_handle_html_tests/\d{10}.txt')

        self.assertEqual(gravar.__annotations__, {'code': (str, bytes), 'filename': str, 'mode': str, 'return': bool})
        conteudo = 'conteúdo de teste\n'
        self.assertTrue(gravar(conteudo, filename))
        with open(filename) as f:
            self.assertEqual(f.read(), conteudo)

        conteudo = b'conte\xc3\xbado de teste\n'
        self.assertTrue(gravar(conteudo, filename))
        with open(filename, 'rb') as f:
            self.assertEqual(f.read(), conteudo)

    def test_content(self):
        self.assertIsNotNone(get_content(self.url))

    def test_get_content(self):
        """
        test_get_content:

        """
        self.assertEqual(get_content(self.url), self.req.content)

    def test_save_content(self):
        """
        test_save_content:
        Valida a implementação do metodo save_content e a gravação do conteudo no local correto
        """
        try:
            output = os.path.abspath(os.path.join(*"incolumepy/static_html/atos/l8666-txtSF.html".split("/")))
            assert os.path.isfile(output), f"Ops: {output}"
        except AssertionError:
            output = os.path.abspath(os.path.join(*"../incolumepy/static_html/atos/l8666-txtSF.html".split("/")))

        self.assertIsInstance(save_content, partial)
        with mock.patch("builtins.open", create=False) as mock_open:
            save_content('html text')
            self.assertEqual(mock.call(output, 'w'), mock_open.call_args)
            self.assertTrue(mock_open.called)
        with mock.patch("builtins.open", create=False) as mock_open:
            save_content(get_content(self.url))
            self.assertEqual(mock.call(output, 'wb'), mock_open.call_args)
            self.assertTrue(mock_open.called)

    def test_text_identify_recover(self):
        """test_text_identify_recover: Grave em outro arquivo somente o conteúdo principal um HTML puro de texto
        limpo """
        try:
            pathfile = os.path.abspath(os.path.join(*"../incolumepy/static_html/atos/l8666-txtSF.html".split("/")))
            assert os.path.isfile(pathfile), f"Ops: {pathfile}"
            output = os.path.abspath(os.path.join(*"../incolumepy/static_html/atos/l8666-original.html".split("/")))
        except AssertionError:
            pathfile = os.path.abspath(os.path.join(*"incolumepy/static_html/atos/l8666-txtSF.html".split("/")))
            output = os.path.abspath(os.path.join(*"incolumepy/static_html/atos/l8666-original.html".split("/")))

        save_content(get_content(self.url))
        self.assertEqual(identify_recover.__annotations__, {'pathfile': str, 'return': str})
        result = identify_recover(pathfile)
        self.assertIsInstance(result, bytes)
        self.assertEqual(168065, len(result))
        self.assertTrue(os.path.isfile(output))

        sha1 = hashlib.sha1()
        sha1.update(result)
        assert "79a42e4056b56d1a2e8528cb0274a0415361db4f" == sha1.hexdigest(),\
            "Ops: Arquivo diverge do esperado. Limpe-o completamente!"

    def test_formating(self):
        """Converter para HTML5, em ascii puro, aplicar CSS legis_03.css ao l8666-original.html,
         inserir cabeçalho no topo do body
        <header>
          <h1> Presidência da República</h1> <h2>Secretaria Geral</h2> <h3>Subchefia para Assuntos Jurídicos</h3>
        </header>
        Aplicar classes CSS (epigrafe, ementa, presidente, ministro (a cada ministro), dou) ao documento
         e salvar o resultado em static_html/atos/l8666.html"""
        try:
            pathfile = os.path.abspath(os.path.join(*"../incolumepy/static_html/atos/l8666-original.html".split("/")))
            assert os.path.isfile(pathfile), f"Ops: {pathfile}"
            output = os.path.abspath(os.path.join(*"../incolumepy/static_html/atos/l8666.html".split("/")))
        except AssertionError:
            pathfile = os.path.abspath(os.path.join(*"incolumepy/static_html/atos/l8666-original.html".split("/")))
            output = os.path.abspath(os.path.join(*"incolumepy/static_html/atos/l8666.html".split("/")))

        self.assertEqual(formating.__annotations__, {'pathfile': str, 'return': str})
        result = formating(pathfile)
        self.assertIsInstance(result, bytes)
        self.assertEqual(168481, len(result))
        self.assertTrue(os.path.isfile(output))
        sha1 = hashlib.sha1()
        sha1.update(result)
        print(sha1.hexdigest())
        assert "50c1e25f5ce415da496c26e99fa57f14d1f4d2c6" == sha1.hexdigest(), \
            "Ops: Arquivo diverge do esperado. Formate-o completamente!"


if __name__ == '__main__':
    unittest.main()
