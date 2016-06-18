dct = {'RN': 'Rio Grande do Norte', 'RJ': 'Rio de Janeiro', 'SP': 'São Paulo'}

# itera por padrão nas chaves
for i in dct:
    print(i, dct[i])

# itera somente nos valores
for v in dct.values():
    print(v)

# items para iterar nos items, onde item é composta por chave e valor
novo_dct = {chave: valor + ': estado do brasil'
            for chave, valor in dct.items() if chave.startswith('R')}

print(novo_dct)
