tpl = (7, 1, 2, 3, 4, 4, 5, 6, 7)

for e in tpl:
    print(e)

cjt = set(tpl)
print(cjt)
pares = {0, 2, 4, 6, 8}

print(cjt.intersection(pares))
print(cjt - pares)
print(cjt.union(pares))
print(1 in cjt)

l = [2, 6, 6, 4, 4, 6, 1, 4, 2, 2, 453534535345]
lookup = set()
nao_repetidos_na_ordem_original = []

for n in l:
    if n not in lookup:
        nao_repetidos_na_ordem_original.append(n)
        lookup.add(n)

print(nao_repetidos_na_ordem_original)

# [1, 2, 4, 6]
