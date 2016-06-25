"""
>>> g = enumerar(range(3), inicio=1)
>>> next(g)
(1, 0)
>>> next(g)
(2, 1)
>>> next(g)
(3, 2)
>>> next(g)
Traceback (most recent call last):
  ...
StopIteration

"""


def infinito(inicio):
    while True:
        yield inicio
        inicio += 1


def enumerar(iteravel, inicio):
    yield from zip(infinito(inicio), iteravel)

