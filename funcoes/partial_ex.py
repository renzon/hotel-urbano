from functools import partial


def soma(a, b):
    return a + b


def mais_dois(a):
    return soma(a, 2)


mais_dois_partial = partial(soma, b=2)

print(mais_dois_partial(2))
print(mais_dois_partial(4))
