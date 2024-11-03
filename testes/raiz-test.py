import unittest
from funções.raiz import raiz

class RaizTest(unittest.TestCase):
    def teste_raiz(self):
        self.assertEqual(raiz(8,3), 2)