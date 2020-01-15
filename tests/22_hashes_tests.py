import unittest
import os

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        base = os.path.dirname(__file__)
        cls.file1 = os.path.join(base, 'static_html', 'css', 'legis_3.css')

    def test_hash_0(self):
        self.assertEqual('abc', hash_md5_0(self.file1))


if __name__ == '__main__':
    unittest.main()
