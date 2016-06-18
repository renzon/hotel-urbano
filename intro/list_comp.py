lista = list(range(10))

print(lista)

lista_por_10 = []

for n in lista:
    if n % 2 == 0:
        lista_por_10.append(10 * n)

print(lista_por_10)

lista_por_10_v2 = [10 * i for i in lista if i % 2 == 0]

print(lista_por_10_v2)
