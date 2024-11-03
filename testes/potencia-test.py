import unittest
from funções.potencia import potencia

class TestPotencia(unittest.TestCase):
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(3, 2), 9)
