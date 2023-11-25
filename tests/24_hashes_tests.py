"""# TODO: Atividade  24: Hash
Proceder com as implementações necessárias para que passe nos testes."""
__author__ = '@britodfbr'
import os
import unittest
from pathlib import Path

from incolume.py.tdd.utils.handlers_hashes import hash_md5_0, hash_sha1_0


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        base = Path(__file__).parent.parent
        cls.file1 = base.joinpath(
            'incolume',
            'py',
            'static_html',
            'css',
            'legis_3.css',
        )
        assert os.path.isfile(cls.file1), f'Ops: {cls.file1}'

    def test_hash_0(self):
        assert hash_md5_0(self.file1) == '4a20ac65a1bb3a9b003d87e1516d13e8'

    def test_hash_1(self):
        assert (
            hash_sha1_0(self.file1)
            == 'a2cd1a8c06db560df912575bb25f88825ec0bded'
        )


if __name__ == '__main__':
    unittest.main()
