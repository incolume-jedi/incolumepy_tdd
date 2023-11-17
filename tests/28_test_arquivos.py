import unittest
import tempfile
import pathlib
import magic
import mimetypes
from src.incolumepy.tdd import arquivos

# TODO: Atividade  28: Proceder com as implementações necessárias para que passe nos testes


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

    @unittest.skip('desable')
    def test_mime(self):
        arquivos.txt_create(self.fout)
        mime = magic.Magic(mime=True)
        self.assertEqual(mime.from_file(self.fout), 'text/plain')

    @unittest.skip
    def test_mimetype(self):
        self.assertTrue(arquivos.txt_create(self.fout))
        self.assertEqual(mimetypes.read_mime_types(self.fout), 'text/plain')


class MyCSVFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(tempfile.NamedTemporaryFile(suffix='.csv').name)
        self.package = pathlib.Path().joinpath('..', 'src', 'incolumepy', 'tdd', 'arquivos').resolve()

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        self.assertFalse(self.fout.exists())
        self.assertEqual(arquivos.csv_create(self.fout), True)
        self.assertTrue(self.fout.is_file())

    @unittest.skip
    def test_mimetype(self):
        self.assertTrue(arquivos.csv_create(self.fout))
        self.assertTrue(pathlib.Path(self.fout).is_file())
        mime = magic.Magic(mime=True)
        resutl = mime.from_file(self.fout)
        self.assertEqual(resutl, 'application/csv')

    @unittest.skip
    def test_mimetype(self):
        self.assertTrue(arquivos.csv_create(self.fout))
        # self.assertEqual(mimetypes.read_mime_types(self.fout), 'application/csv')
        self.assertEqual(mimetypes.MimeTypes(self.fout), 'application/csv')


class MyJsonFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(tempfile.NamedTemporaryFile(suffix='.json').name)
        self.package = pathlib.Path().joinpath('..', 'src', 'incolumepy', 'tdd', 'arquivos').resolve()

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        self.assertFalse(self.fout.exists())
        self.assertEqual(arquivos.json_create(self.fout), True)
        self.assertTrue(self.fout.is_file())

    @unittest.skip
    def test_mimetype(self):
        arquivos.csv_create(self.fout)
        mime = magic.Magic(mime=True)
        self.assertEqual(mime.from_file(self.fout), 'application/json')


class MyXLSXFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fout = pathlib.Path(tempfile.NamedTemporaryFile(suffix='.xlsx').name)
        self.package = pathlib.Path().joinpath('..', 'src', 'incolumepy', 'tdd', 'arquivos').resolve()

    def test_package(self):
        assert self.package.is_dir(), f'{self.package}'

    def test_create(self):
        self.assertFalse(self.fout.exists())
        self.assertEqual(arquivos.xlsx_create(self.fout), True)
        self.assertTrue(self.fout.is_file())

    @unittest.skip
    def test_mimetype(self):
        arquivos.csv_create(self.fout)
        mime = magic.Magic(mime=True)
        self.assertEqual(mime.from_file(self.fout), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


if __name__ == '__main__':
    unittest.main()
