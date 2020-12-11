import unittest
import tempfile
import pathlib
from src.incolumepy.tdd import arquivos


class MyTextFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(tempfile.NamedTemporaryFile(suffix='.txt').name)
        self.package = pathlib.Path().joinpath('..', 'src', 'incolumepy', 'tdd', 'arquivos').resolve()

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        self.assertFalse(self.fout.exists())
        self.assertEqual(arquivos.txt_create(self.fout), True)
        self.assertTrue(self.fout.is_file())

    def test_content(self):
        self.assertTrue(arquivos.txt_create(self.fout))
        self.assertGreaterEqual(len(self.fout.read_text().split('\n')), 100)
        self.assertGreater(len(self.fout.read_text()), 1500)


if __name__ == '__main__':
    unittest.main()
