import unittest
from funções.divisao import dividir

class DivisaoTest(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(10,2), 5)