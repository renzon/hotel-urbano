import unittest
from unittest.mock import Mock

from ghhu.telefonista import Telefonista


class TelefonistaTestesBasicos(unittest.TestCase):
    def setUp(self):
        self.telefonista = Telefonista()
        self.telefone_mock = Mock()
        self.telefone_mock.telefonar = Mock(return_value='Ligando de mentira para 2345678')
        self.telefonista._telefone = self.telefone_mock
        self.telefonista.adicionar_contato('Renzo', '2345678')

    def teste_adicionar_um_contato(self):
        telefonista = Telefonista()
        telefonista.adicionar_contato('Renzo', '2345678')
        self.assertEqual([('Renzo', '2345678')], telefonista._contatos)

    def teste_ligar_para_todos_contatos(self):
        ligacao_feita = self.telefonista.ligar_para_todos_contatos()
        self.assertListEqual(['Ligando de mentira para 2345678 - Renzo'], ligacao_feita)
        self.telefone_mock.telefonar.assert_called_once_with('2345678')

    def test_ligar_para_dois_contatos(self):
        self.telefonista.adicionar_contato('Henrique', '8765432')

        def telefonar(numero):
            return 'Ligando de mentira para %s' % numero

        self.telefone_mock.telefonar.side_effect = telefonar

        ligacoes_feitas = self.telefonista.ligar_para_todos_contatos()
        self.assertListEqual(['Ligando de mentira para 2345678 - Renzo',
                              'Ligando de mentira para 8765432 - Henrique'], ligacoes_feitas)
        self.assertEqual(2, self.telefone_mock.telefonar.call_count)
        self.telefone_mock.telefonar.assert_any_call('2345678')
        self.telefone_mock.telefonar.assert_any_call('8765432')


class TelefonistaTestesIntegracao(unittest.TestCase):
    def teste_ligar_para_todos_contatos(self):
        telefonista = Telefonista()
        telefonista.adicionar_contato('Renzo', '2345678')
        ligacao_feita = telefonista.ligar_para_todos_contatos()
        self.assertListEqual(['Ligando de verdade para 2345678 - Renzo'], ligacao_feita)
        telefonista.adicionar_contato('Henrique', '8765432')
        ligacoes_feitas = telefonista.ligar_para_todos_contatos()
        self.assertListEqual(['Ligando de verdade para 2345678 - Renzo',
                              'Ligando de verdade para 8765432 - Henrique'], ligacoes_feitas)
