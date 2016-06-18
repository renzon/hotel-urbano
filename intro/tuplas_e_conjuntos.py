tpl = (7, 1, 2, 3, 4, 4, 5, 6, 7)

for e in tpl:
    print(e)

cjt = set(tpl)
print(cjt)
pares = {0, 2, 4, 6, 8}

print(cjt.intersection(pares))
print(cjt-pares)
print(cjt.union(pares))
print(1 in cjt)
