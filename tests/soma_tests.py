import unittest

from ghhu.soma import soma


class SomaTests(unittest.TestCase):
    def teste_soma_zero(self):
        resultado = soma(0, 0)
        self.assertEqual(0, resultado)

    def test_soma_neutra(self):
        self.assertEqual(1, soma(1, 0))
        self.assertEqual(2, soma(2, 0))


if __name__ == '__main__':
    unittest.main()
