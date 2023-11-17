#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade  28: Proceder com as implementações necessárias para que passe nos testes

"""
__author__ = '@britodfbr'
import unittest
import tempfile
import pathlib
import magic
import mimetypes
import pandas as pd
from src.incolumepy.tdd import arquivos


class MyTextFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(tempfile.NamedTemporaryFile(suffix='.txt').name)
        self.package = pathlib.Path(__file__).parent.joinpath('..', 'src', 'incolumepy', 'tdd', 'arquivos').resolve()

    @unittest.skip
    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        self.assertFalse(self.fout.exists())
        self.assertEqual(arquivos.txt_create(self.fout), True)
        self.assertTrue(self.fout.is_file())

    def test_length(self):
        self.assertTrue(arquivos.txt_create(self.fout))
        self.assertGreaterEqual(len(self.fout.read_text().split('\n')), 100)
        self.assertGreater(len(self.fout.read_text()), 1500)

    def test_content(self):
        self.assertTrue(arquivos.txt_create(self.fout))
        self.assertIn('verde claro', self.fout.read_text())
        self.assertIn('azul escuro', self.fout.read_text())

    @unittest.skip('desable')
    def test_mimetype_magic(self):
        arquivos.txt_create(self.fout)
        mime = magic.Magic(mime=True)
        self.assertEqual(mime.from_file(self.fout), 'text/plain')

    def test_mimetype(self):
        self.assertTrue(arquivos.txt_create(self.fout))
        self.assertIn('text/plain', mimetypes.guess_type(self.fout))


class MyCSVFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(tempfile.NamedTemporaryFile(suffix='.csv').name)
        self.package = pathlib.Path(__file__).parent.joinpath('..', 'src', 'incolumepy', 'tdd', 'arquivos').resolve()

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        self.assertFalse(self.fout.exists())
        self.assertEqual(arquivos.csv_create(self.fout), True)
        self.assertTrue(self.fout.is_file())

    def test_length(self):
        self.assertTrue(arquivos.csv_create(self.fout))
        df = pd.read_csv(self.fout)
        self.assertGreaterEqual(df.shape[0], 100)
        self.assertGreater(df.shape[0], 1500)

    def test_content(self):
        self.assertTrue(arquivos.csv_create(self.fout))
        self.assertIn('verde claro', self.fout.read_text())
        self.assertIn('azul escuro', self.fout.read_text())

    @unittest.skip('desable')
    def test_mimetype_magic(self):
        self.assertTrue(arquivos.csv_create(self.fout))
        self.assertTrue(pathlib.Path(self.fout).is_file())
        mime = magic.Magic(mime=True)
        resutl = mime.from_file(self.fout)
        self.assertEqual(resutl, 'application/csv')

    def test_mimetype(self):
        self.assertTrue(arquivos.csv_create(self.fout))
        self.assertIn('text/csv', mimetypes.guess_type(self.fout))


class MyJsonFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(tempfile.NamedTemporaryFile(suffix='.json').name)
        self.package = pathlib.Path(__file__).parent.joinpath('..', 'src', 'incolumepy', 'tdd', 'arquivos').resolve()

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        self.assertFalse(self.fout.exists())
        self.assertEqual(arquivos.json_create(self.fout), True)
        self.assertTrue(self.fout.is_file())

    def test_length(self):
        self.assertTrue(arquivos.json_create(self.fout))
        df = pd.read_json(self.fout)
        self.assertGreaterEqual(df.shape[0], 100)
        self.assertGreater(df.shape[0], 1500)

    def test_content(self):
        self.assertTrue(arquivos.json_create(self.fout))
        self.assertIn('verde claro', self.fout.read_text())
        self.assertIn('azul escuro', self.fout.read_text())

    @unittest.skip('desable')
    def test_mimetype_magic(self):
        arquivos.json_create(self.fout)
        mime = magic.Magic(mime=True)
        self.assertEqual(mime.from_file(self.fout), 'application/json')

    def test_mimetype(self):
        self.assertTrue(arquivos.json_create(self.fout))
        self.assertIn('application/json', mimetypes.guess_type(self.fout))


class MyXLSXFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(tempfile.NamedTemporaryFile(suffix='.xlsx').name)
        self.package = pathlib.Path(__file__).parent.joinpath('..', 'src', 'incolumepy', 'tdd', 'arquivos').resolve()

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        self.assertFalse(self.fout.exists())
        self.assertEqual(arquivos.xlsx_create(self.fout), True)
        self.assertTrue(self.fout.is_file())

    def test_length(self):
        self.assertTrue(arquivos.xlsx_create(self.fout))
        df = pd.read_excel(self.fout, engine='openpyxl')
        self.assertGreaterEqual(df.shape[0], 100)
        self.assertGreater(df.shape[0], 1500)

    def test_content(self):
        self.assertTrue(arquivos.xlsx_create(self.fout))
        df = pd.read_excel(self.fout, engine='openpyxl')
        self.assertIn('azul escuro', df.iloc[0, 1])
        self.assertIn('verde claro', df.iloc[0, 2])

    @unittest.skip('desable')
    def test_mimetype_magic(self):
        arquivos.xlsx_create(self.fout)
        mime = magic.Magic(mime=True)
        self.assertEqual(mime.from_file(self.fout), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    def test_mimetype(self):
        self.assertTrue(arquivos.xlsx_create(self.fout))
        self.assertIn(
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            mimetypes.guess_type(self.fout)
        )


if __name__ == '__main__':
    unittest.main()
