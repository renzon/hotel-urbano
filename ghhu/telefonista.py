from ghhu.telefone import Telefone


class Telefonista:
    def __init__(self):
        self._telefone = Telefone()
        self._contatos = []

    def adicionar_contato(self, nome, numero):
        self._contatos.append((nome, numero))

    def ligar_para_todos_contatos(self, telefone=None):
        tel = self._telefone if telefone is None else telefone
        return ['{msg_telefone} - {contato}'.format(msg_telefone=tel.telefonar(numero), contato=nome)
                for nome, numero in self._contatos]
