cc = list(range(16))

INICIO = slice(4)
n = len(cc)
FIM = slice(- 4, None)
mascara = ['*'] * (n - 8)
cc_obfuscado = cc[INICIO] + mascara + cc[FIM]
print(cc_obfuscado)

cc[4:-4] = mascara
print(cc)
