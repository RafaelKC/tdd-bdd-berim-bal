import unittest
from funções.multiplicacao import multiplicar

class MultiplicacaoTest(unittest.TestCase):
    def test_multiplicacao(self):
        self.assertEqual(multiplicar(10,2), 20)