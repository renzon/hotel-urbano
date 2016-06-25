import operator


class Pessoa():
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome

    def __repr__(self):
        return 'Pessoa({!r},{!r})'.format(self.nome, self.idade)


pessoas = [Pessoa('Diego', 18), Pessoa('Raissa', 19), Pessoa('Renzo', 33)]

print(sorted(pessoas, key=lambda p: p.idade))
print(sorted(pessoas, key=operator.attrgetter('idade')))

print(operator.getitem(pessoas,0))

