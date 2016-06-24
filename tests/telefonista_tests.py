import unittest

from ghhu.telefonista import Telefonista


class TelefonistaTestesBasicos(unittest.TestCase):
    def teste_adicionar_um_contato(self):
        telefonista = Telefonista()
        telefonista.adicionar_contato('Renzo', '2345678')
        self.assertEqual([('Renzo', '2345678')], telefonista._contatos)

    def teste_ligar_para_todos_contatos(self):
        class TelefoneMock():
            def telefonar(self, numero):
                return 'Ligando de mentira para %s' % numero

        telefone_mock = TelefoneMock()
        telefonista = Telefonista()
        telefonista.adicionar_contato('Renzo', '2345678')
        ligacao_feita = telefonista.ligar_para_todos_contatos(telefone=telefone_mock)
        self.assertListEqual(['Ligando de mentira para 2345678 - Renzo'], ligacao_feita)
        telefonista.adicionar_contato('Henrique', '8765432')
        ligacoes_feitas = telefonista.ligar_para_todos_contatos(telefone=telefone_mock)
        self.assertListEqual(['Ligando de mentira para 2345678 - Renzo',
                              'Ligando de mentira para 8765432 - Henrique'], ligacoes_feitas)


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
