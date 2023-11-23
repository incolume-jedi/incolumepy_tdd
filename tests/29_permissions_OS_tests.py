#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# TODO: Atividade 29: Proceder com as implementações necessárias para que passe nos testes

Criação de arquivos/diretórios no sistema operacional através do Python com permissões específicas,
 para leitura, escrita, execução.
"""
__author__ = '@britodfbr'
import unittest
import os
import platform
from .BaseTests import BaseTestCase
from pathlib import Path
from incolumepy.tdd.permissions.genfile import create


class MyTestCase(BaseTestCase):
    def test_create_assign(self):
        self.assertEqual(
            create.__annotations__,
            {'content': (str, bytes), 'filename': (str, Path), 'permissions': str, 'return': bool}
        )

    def test_create_permission_length(self):
        with self.assertRaisesRegex(AttributeError, 'Bad permission length'):
            create(self.content, self.filename, '')

        create(self.content, self.filename, '---------')

    def test_create_file_created(self):
        self.assertFalse(self.filename.is_file())
        self.assertTrue(create(self.content, self.filename, 'rwx------'))
        self.assertTrue(self.filename.is_file())

    def test_create_content_str(self):
        self.assertTrue(create(self.content, self.filename, 'rwx------'))
        self.assertTrue(self.filename.is_file())
        self.assertIsInstance(self.filename.read_text(), str)

    def test_create_content_bytes(self):
        self.assertTrue(create(str.encode(self.content), self.filename, 'rwx------'))
        self.assertTrue(self.filename.is_file())
        self.assertIsInstance(self.filename.read_bytes(), bytes)

    def test_create_content_raises(self):
        with self.assertRaisesRegex(TypeError, 'data must be str, not int'):
            create(1111, self.filename, 'rwx')

        with self.assertRaisesRegex(TypeError, 'data must be str, not float'):
            create(11.11, self.filename, 'rwx')

        with self.assertRaisesRegex(TypeError, 'data must be str, not list'):
            create([], self.filename, 'rwx')

        with self.assertRaisesRegex(TypeError, 'data must be str, not tuple'):
            create(('', ), self.filename, 'rwx')

        with self.assertRaisesRegex(TypeError, 'data must be str, not dict'):
            create({}, self.filename, 'rwx')

    def test_nopermition(self):
        create(str.encode(self.content), self.filename, '---------')
        self.assertFalse(os.access(self.filename, os.R_OK))
        self.assertFalse(os.access(self.filename, os.W_OK))
        self.assertFalse(os.access(self.filename, os.X_OK))

    def test_permition_read(self):
        # Validação de permissões: Read
        tests = [
            self.t('r--r--r--', True),
            self.t('r--------', True),
            self.t('r--r-----', True),
            self.t('r-----r--', True),
            self.t('------r--', False),
            self.t('---r--r--', False),
        ]
        for test in tests:
            # print(test.entrance)
            create(str.encode(self.content), self.filename, test.entrance)
            # self.assertTrue(os.access(self.filename, os.R_OK))
            result = os.access(self.filename, os.R_OK)
            self.assertEqual(test.expected, result)
            self.filename.unlink()

        create(str.encode(self.content), self.filename, 'r--------')
        self.assertTrue(os.access(self.filename, os.R_OK))
        self.filename.unlink()

    def test_permition_exec(self):
        # Validação de permissões: Excution
        create(str.encode(self.content), self.filename, 'x--------')
        self.assertTrue(os.access(self.filename, os.X_OK))
        self.assertFalse(os.access(self.filename, os.R_OK))
        self.assertFalse(os.access(self.filename, os.W_OK))

    def test_permition_write(self):
        # Validação de permissões: Write
        create(str.encode(self.content), self.filename, 'w--------')
        self.assertTrue(os.access(self.filename, os.W_OK))
        self.assertFalse(os.access(self.filename, os.R_OK))
        self.assertFalse(os.access(self.filename, os.X_OK))


if __name__ == '__main__':
    unittest.main()
