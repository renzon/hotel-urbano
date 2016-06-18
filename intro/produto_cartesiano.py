from itertools import product

qtdes = [2, 3, 4, 5, 6]
frutas = 'caqui banana abacaxi morango pequi'.split()

# Newbie
for i in range(len(qtdes)):
    print(qtdes[i], frutas[i])

# Intemediário

for i, v in enumerate(qtdes):
    print(v, frutas[i])

# Melhor

for q, f in zip(qtdes, frutas):
    print(q, f)

# Mudando de assunto, produto cartesiano

produto = []
for q in qtdes:
    for f in frutas:
        produto.append([q, f])

print(produto)

produto_2 = [[q, f] for q in qtdes for f in frutas]

print(produto_2)

print(list(product(qtdes,frutas)))
