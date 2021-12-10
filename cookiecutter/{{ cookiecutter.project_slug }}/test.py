from .__main__ import do, do2
from unittest import TestCase
from os import path

class Test(TestCase):

    def setUp(self) -> None:
        self.test_path = path.join(path.dirname(path.abspath(__file__)), 'test.txt')
        return super().setUp()

    def test_do(self):
        self.assertEqual(str(do(self.test_path)), '')

    def test_do2(self):
        self.assertEqual(str(do2(self.test_path)), '')
