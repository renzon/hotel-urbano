frutas = 'caqui banana abacaxi morango pequi'.split()

frutas_revertidas = reversed(frutas)

print(max(frutas_revertidas, key=len))

tamanhos = [len(f) for f in frutas]
frutas_peso = list(zip(tamanhos, range(10, 0, -1), frutas))
print(frutas_peso)

print(sorted(frutas_peso))
