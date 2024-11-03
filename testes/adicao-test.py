import unittest
from funções.adicao import somar

class AdicaoTest(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(somar(100, 100), 200)