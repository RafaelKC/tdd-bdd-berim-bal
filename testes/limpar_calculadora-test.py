import unittest
from funções.limpar_calculadora import limpar_calculadora

class TestLimparCalculadora(unittest.TestCase):
    def test_limpar_calculadora(self):
        self.assertEqual(limpar_calculadora(), 0)