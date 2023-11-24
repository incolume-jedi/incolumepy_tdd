#!/usr/bin/env python
"""# TODO: Atividade  28: Proceder com as implementações necessárias
para que passe nos testes.
"""
__author__ = '@britodfbr'
import mimetypes
import pathlib
import tempfile
import unittest

import magic
import pandas as pd
from incolume.py.tdd import arquivos


class MyTextFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(
            tempfile.NamedTemporaryFile(suffix='.txt').name,
        )
        self.package = (
            pathlib.Path(__file__)
            .parents[1]
            .joinpath('incolume', 'py', 'tdd', 'arquivos')
            .resolve()
        )

    # @unittest.skip
    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        assert not self.fout.exists()
        assert arquivos.txt_create(self.fout) is True
        assert self.fout.is_file()

    def test_length(self):
        assert arquivos.txt_create(self.fout)
        assert len(self.fout.read_text().split('\n')) >= 100
        assert len(self.fout.read_text()) > 1500

    def test_content(self):
        assert arquivos.txt_create(self.fout)
        assert 'verde claro' in self.fout.read_text()
        assert 'azul escuro' in self.fout.read_text()

    # @unittest.skip('desable')
    def test_mimetype_magic(self):
        arquivos.txt_create(self.fout)
        mime = magic.Magic(mime=True)
        assert mime.from_file(self.fout) == 'text/csv'

    def test_mimetype(self):
        assert arquivos.txt_create(self.fout)
        assert 'text/plain' in mimetypes.guess_type(self.fout)


class MyCSVFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(
            tempfile.NamedTemporaryFile(suffix='.csv').name,
        )
        self.package = (
            pathlib.Path(__file__)
            .parents[1]
            .joinpath('incolume', 'py', 'tdd', 'arquivos')
            .resolve()
        )

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        assert not self.fout.exists()
        assert arquivos.csv_create(self.fout) is True
        assert self.fout.is_file()

    def test_length(self):
        assert arquivos.csv_create(self.fout)
        df = pd.read_csv(self.fout)
        assert df.shape[0] >= 100
        assert df.shape[0] > 1500

    def test_content(self):
        assert arquivos.csv_create(self.fout)
        assert 'verde claro' in self.fout.read_text()
        assert 'azul escuro' in self.fout.read_text()

    # @unittest.skip('desable')
    def test_mimetype_magic(self):
        assert arquivos.csv_create(self.fout)
        assert pathlib.Path(self.fout).is_file()
        mime = magic.Magic(mime=True)
        resutl = mime.from_file(self.fout)
        assert resutl == 'text/csv'

    def test_mimetype(self):
        assert arquivos.csv_create(self.fout)
        assert 'text/csv' in mimetypes.guess_type(self.fout)


class MyJsonFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(
            tempfile.NamedTemporaryFile(suffix='.json').name,
        )
        self.package = (
            pathlib.Path(__file__)
            .parents[1]
            .joinpath('incolume', 'py', 'tdd', 'arquivos')
            .resolve()
        )

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        assert not self.fout.exists()
        assert arquivos.json_create(self.fout) is True
        assert self.fout.is_file()

    def test_length(self):
        assert arquivos.json_create(self.fout)
        df = pd.read_json(self.fout)
        assert df.shape[0] >= 100
        assert df.shape[0] > 1500

    def test_content(self):
        assert arquivos.json_create(self.fout)
        assert 'verde claro' in self.fout.read_text()
        assert 'azul escuro' in self.fout.read_text()

    # @unittest.skip('desable')
    def test_mimetype_magic(self):
        arquivos.json_create(self.fout)
        mime = magic.Magic(mime=True)
        assert mime.from_file(self.fout) == 'application/json'

    def test_mimetype(self):
        assert arquivos.json_create(self.fout)
        assert 'application/json' in mimetypes.guess_type(self.fout)


class MyXLSXFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(
            tempfile.NamedTemporaryFile(suffix='.xlsx').name,
        )
        self.package = (
            pathlib.Path(__file__)
            .parents[1]
            .joinpath('incolume', 'py', 'tdd', 'arquivos')
            .resolve()
        )

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        assert not self.fout.exists()
        assert arquivos.xlsx_create(self.fout) is True
        assert self.fout.is_file()

    def test_length(self):
        assert arquivos.xlsx_create(self.fout)
        df = pd.read_excel(self.fout, engine='openpyxl')
        assert df.shape[0] >= 100
        assert df.shape[0] > 1500

    def test_content(self):
        assert arquivos.xlsx_create(self.fout)
        df = pd.read_excel(self.fout, engine='openpyxl')
        assert 'azul escuro' in df.iloc[0, 1]
        assert 'verde claro' in df.iloc[0, 2]

    # @unittest.skip('desable')
    def test_mimetype_magic(self):
        arquivos.xlsx_create(self.fout)
        mime = magic.Magic(mime=True)
        assert (
            mime.from_file(self.fout)
            == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

    def test_mimetype(self):
        assert arquivos.xlsx_create(self.fout)
        assert (
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            in mimetypes.guess_type(self.fout)
        )


if __name__ == '__main__':
    unittest.main()
