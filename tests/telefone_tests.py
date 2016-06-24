import unittest

from ghhu.telefone import Telefone


class TelefoneTests(unittest.TestCase):
    def test_telefonar(self):
        telefone = Telefone()
        resultado = telefone.telefonar('2345678')
        self.assertEqual('Ligando de verdade para 2345678', resultado)
