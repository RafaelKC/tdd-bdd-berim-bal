import unittest
from funções.subtracao import subtrair

class SubtrairTest(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(subtrair(200, 100), 100)