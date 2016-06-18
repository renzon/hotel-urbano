import io

with io.open('estados.txt', mode='w', encoding='utf8') as f:
    f.write('RN\nSP\nRJ')

with io.open('estados.txt', mode='r', encoding='utf8') as f:
    for linha in f:
        print(linha.strip())
