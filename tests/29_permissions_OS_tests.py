"""# TODO: Atividade 29: Permissões em arquivos.
Proceder com as implementações necessárias para que passe nos testes

Criação de arquivos/diretórios no sistema operacional através
do Python com permissões específicas, para leitura, escrita, execução.
"""
__author__ = '@britodfbr'

import os

import pytest
import platform
from pathlib import Path
from incolume.py.tdd.permissions.genfile import create
from tempfile import NamedTemporaryFile


class TestPermission:
    """Test Permission dataclass."""


class TestCase:
    """TestCase."""

    def test_create_annotation(self) -> None:
        """Test create_assign."""
        assert create.__annotations__ == {
            'content': (str, bytes),
            'filename': (str, Path),
            'permissions': str,
            'return': bool,
        }

    @pytest.mark.parametrize(
        'filename permission'.split(),
        [
            (NamedTemporaryFile().name, ''),
            (Path(NamedTemporaryFile().name), ''),
            (NamedTemporaryFile().name, '-------'),
            (Path(NamedTemporaryFile().name), '--------'),
        ],
    )
    def test_create_permission_length(
        self,
        loremipsum,
        filename,
        permission,
    ) -> None:
        with pytest.raises(AttributeError, match='Bad permission length'):
            create(loremipsum, filename, permission)

    def test_create_file_created(self, loremipsum) -> None:
        """Test it."""
        assert create(loremipsum, NamedTemporaryFile().name, 'rwx------')

    def test_create_content_str(self, loremipsum) -> None:
        """Test it."""
        filename = Path(NamedTemporaryFile().name)
        create(loremipsum, filename, 'rwx------')
        assert isinstance(filename.read_text(), str)

    def test_create_content_bytes(self, loremipsum) -> None:
        """Test it."""
        filename = Path(NamedTemporaryFile().name)
        create(str.encode(loremipsum), filename, 'rwx------')
        assert isinstance(filename.read_bytes(), bytes)

    @pytest.mark.parametrize(
        'entrance',
        [
            1111,
            11.11,
            [],
            ('',),
            {},
        ],
    )
    def test_create_content_raises(self, entrance):
        """Exceptions."""
        filename = Path(NamedTemporaryFile().name)
        with pytest.raises(
            TypeError, match=f'data must be str, not {type(entrance).__name__}'
        ):
            create(entrance, filename, 'rwx')

    @pytest.mark.parametrize(
        'permission',
        [
            os.R_OK,
            os.W_OK,
            os.X_OK,
        ],
    )
    def test_nopermition(self, loremipsum, permission) -> None:
        filename = Path(NamedTemporaryFile().name)
        create(str.encode(loremipsum), filename, '---------')
        assert not os.access(filename, permission)

    @pytest.mark.parametrize(
        'f_perm os_perm expected'.split(),
        [
            ('w--------', os.W_OK, True),
            ('w--------', os.R_OK, False),
            ('w--------', os.X_OK, False),
            ('x--------', os.W_OK, False),
            ('x--------', os.R_OK, False),
            ('x--------', os.X_OK, True),
            ('r--------', os.W_OK, False),
            ('r--------', os.R_OK, True),
            ('r--------', os.X_OK, False),
            ('r--r--r--', os.R_OK, True),
            ('r--------', os.R_OK, True),
            ('r--r-----', os.R_OK, True),
            ('r-----r--', os.R_OK, True),
            ('------r--', os.R_OK, False),
            ('---r--r--', os.R_OK, False),
            ('w--w--w--', os.W_OK, True),
            ('---w--w--', os.W_OK, False),
            ('------w--', os.W_OK, False),
            ('--x--x--x', os.X_OK, True),
            ('-----x--x', os.X_OK, False),
            ('--------x', os.X_OK, False),
        ],
    )
    def test_permition(self, loremipsum, f_perm, os_perm, expected) -> None:
        """Validação de permissões."""
        filename = Path(NamedTemporaryFile().name)
        create(str.encode(loremipsum), filename, f_perm)
        assert os.access(filename, os_perm) == expected
