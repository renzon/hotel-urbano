lista = 'caqui banana abacaxi morango pequi'.split()
print(', '.join(lista))



print(sorted(lista))
print(sorted(lista, key=len))


def invertida(palavra):
    return palavra[::-1]


print(sorted(lista, key=invertida))
print(sorted(lista, key=lambda palavra: palavra[::-1]))

print(lista.pop())
lista.insert(0, 'mamao')
print(lista)
# print(frutas.index('nao existe'))
print(lista.index('morango'))
lista.append('morango')
print(lista)
print(lista.remove('morango'))
print(lista)
