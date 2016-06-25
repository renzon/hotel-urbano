def simples():
    print('f 1')
    yield 1
    print('f 2')
    yield 2
    print('f 3')
    yield 3
    print('Finalizando')


g = simples()
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

for i in simples():
    print(i)
