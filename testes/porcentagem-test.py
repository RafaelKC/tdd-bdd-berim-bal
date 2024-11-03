import unittest
from funções.porcentagem import porcentagem

class PorcentagemTest(unittest.TestCase):
    def test_porcentagem(self):
        self.assertEqual(porcentagem(10,50), 5)