import unittest
from src.incolumepy.utils.decode.morse import decodeMorse


class MyTestCase(unittest.TestCase):
    def test_something(self):
        """Example from description"""
        self.assertEqual(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')


if __name__ == '__main__':
    unittest.main()
