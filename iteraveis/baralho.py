from collections import namedtuple
from itertools import product
from random import shuffle

Carta = namedtuple('Carta', 'naipe valor')


# print(type(Carta))

# zap = Carta('Paus', '4')

# print(zap[0])
# print(zap.naipe)

class Baralho():
    naipes = 'paus copas espadas ouros'.split()
    valores = [str(v) for v in range(2, 10)] + 'Q J K A'.split()

    def __init__(self):
        self._cartas = [Carta(*t)
                        for t in product(self.naipes, self.valores)]

    def __repr__(self):
        return repr(self._cartas)

    def __getitem__(self, item):
        return self._cartas[item]

    def __setitem__(self, key, value):
        self._cartas[key] = value

    def __len__(self):
        return len(self._cartas)


baralho = Baralho()

print(baralho)

shuffle(baralho)
for carta in baralho:
    print(carta)

print(baralho[0])
