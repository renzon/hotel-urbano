cc = list(range(16))

INICIO = slice(4)
n = len(cc)
FIM = slice(- 4, None)
cc_obfuscado = cc[INICIO] + (['*'] * (n-8)) + cc[FIM]
print(cc_obfuscado)


