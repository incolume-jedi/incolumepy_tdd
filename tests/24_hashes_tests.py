import unittest
import os
from src.incolumepy.utils.handlers_hashes import hash_md5_0
from src.incolumepy.utils.handlers_hashes import hash_sha1_0


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        base = os.path.dirname(__file__)
        try:
            cls.file1 = os.path.join(base, '..', 'incolumepy', 'static_html', 'css', 'legis_3.css')
            assert os.path.isfile(cls.file1), F"Ops: {cls.file1}"
        except FileNotFoundError:
            cls.file1 = os.path.join(base, 'incolumepy', 'static_html', 'css', 'legis_3.css')

    def test_hash_0(self):
        self.assertEqual('4a20ac65a1bb3a9b003d87e1516d13e8', hash_md5_0(self.file1))

    def test_hash_1(self):
        self.assertEqual('a2cd1a8c06db560df912575bb25f88825ec0bded', hash_sha1_0(self.file1))


if __name__ == '__main__':
    unittest.main()
