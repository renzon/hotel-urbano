import unittest
from datetime import datetime
from unittest.mock import patch

from ghhu.vida import minutos_de_vida


class MinutosDeVidaTests(unittest.TestCase):
    @patch('ghhu.vida.calcular_agora')
    def test_basico(self, agora):
        agora.return_value = datetime(2016, 6, 24, 3, 27, 0)
        minutos = minutos_de_vida(datetime(2016, 6, 24, 3, 26, 0))
        self.assertEqual(1, minutos)

    @patch('ghhu.vida.calcular_agora')
    def test_nao_basico(self, agora):
        agora.return_value = datetime(2016, 6, 24, 3, 27, 0)
        minutos = minutos_de_vida(datetime(2016, 6, 24, 3, 25, 0))
        self.assertEqual(2, minutos)
