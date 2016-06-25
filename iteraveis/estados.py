siglas = ['RJ', 'SP', 'MG']
nomes = ['Rio de Janeiro', 'São Paulo', 'Minas Gerais']

for i in range(len(siglas)):
    print(siglas[i], nomes[i])

for i, sigla in enumerate(siglas):
    print(sigla, nomes[i])

for sigla, nome in zip(siglas, nomes):
    print(sigla, nome)

print(sum(range(10)))


print(list(filter(lambda v: v<=10,map(lambda i: i * 2, range(10)))))

*r, ultimo = range(10)

print(r)
print(ultimo)



